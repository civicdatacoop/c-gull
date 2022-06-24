# Introduction

## Purpose
This document is the Software Requirements Specification for the C-GULL Study Management System.

## Scope
This document describes software requirements as defined in section 8.4 of ISO/IEC/IEEE 29148:2018(E) standard.

Author: David Salac

Organization: Liverpool City Region Civic Data Cooperative (University of Liverpool)

Version: 0.0.1
## Product overview
C-GULL Study Management System (SMS) is the information system that helps organize study participants and stores important information about participants and events related to each participant (like appointments, calls, and notes). Project Children Grown-Up in Liverpool (C-GULL) is a longitudinal study focused on women who are pregnant for the first time. The estimated number of participants is 10000. The estimated number of contacted people is 30000. Technically, it is a web application that interacts with other components, as visualized in Figure 1.

![CGULL_SMS_POSITION.png](CGULL_SMS_POSITION.png)

Figure 1: Position of Study Management System among other components. The eCRF component is responsible for managing consent forms (and other research forms), K2 is an internal hospital system, and the Research environment is a place for analytical research queries (OLAP).

The SMS also provides helpful functionality that makes the study run smoothly (like printing labels for samples or generating Family IDs). In addition, it interacts with external entities: the K2 system that is used for import of potential participants; eCRF (probably implemented using REDCap) that is used for consent forms; the research environment is a database and protected environment that stores data for further analysis.

# System requirements

## Functions
### Overall composition
| ID | Requirement |
| --- | --- |
| F010 | The main functional parts of the system shall be the Participant subsystem, Appointment subsystem, and Administration subsystem. |

_The Participant subsystem and Appointment subsystem have their position in database logic, whereas the Administration subsystem only contains requirements related to the management of the system._

### Participant subsystem
| ID | Requirement |
| --- | --- |
| F020 | The participant subsystem shall store and handle information about all potential and confirmed study participants and provide the functionality to manage them (CRUD operations and other functions). |
| F030 | The participant subsystem shall automatically import all potential participants from K2 once a week. |
| F040 | A potential participant of the study shall be a first-time pregnant woman. |
| F050 | The participant subsystem shall allow manually inserting a voluntary participant using the front-end interface (meaning that mothers can register online voluntarily). |
| F060 | The participant subsystem shall store (and manage) information about each person that includes NHS number, ID in the system (automatically assigned), full name, date of birth, day of death (if applicable), phone number, email address, primary language, processed flag (described below), and other things described separately in this document. |
| F070 | The participant subsystem shall store (and manage) relationships between participants defining important relations - namely: biological mother, biological father, TODO. It also shall contains information about who is entitled to sign consents for the person (if applicable, typically when the participant is an infant) and if this person can sign on her own. |
| F080 | Selected relationships between participants shall define Family entity (which shall define Family ID) – proper relations defining family are chosen manually. |
| F090 | The processed flag shall be true if a person is found either eligible or non-eligible for the study; it shall be false if a person was not reviewed yet by the study administrator. (_It functionally helps filter people who have not been reviewed yet_). |
| F100 | If the person is found eligible, then the first (empty) Appointment shall be created by the Appointment subsystem. (_This empty appointment is factically a flag - it helps filter people that should be contacted by the study team_). |
| F110 | The participant subsystem shall store Notes (defined in the separate subsection) related to each person. |
| F120 | The participant subsystem shall store address history related to each participant (from what time to what time and where a participant lives). |
| F130 | The participant subsystem shall store disability history related to each participant – what is the disability when it started and finished (if applicable). TODO: is it imported from K2? |
| F140 | The participant subsystem shall store demographic history related to each participant (TODO: define what exactly it is), including a timeline of all relevant information. |
| F150 | The participant subsystem shall store information about withdrawal from the study related to participants that opt out of the study (this includes the date and reason why is a person out). |
| F160 | The participant subsystem shall allow deletion of all information related to a particular person (relevant because of GDPR). |

### Notes
| ID | Requirement |
| --- | --- |
| F170 | Notes shall be related to one entity (like Participant, Appointment) – this entity can have none, one or many notes. |
| F180 | Each note shall contain information about the author of the note (User of the system), last update, date of creation, subject (if applicable) and the actual text of the note. |

### Tractability
| ID | Requirement |
| --- | --- |
| F190 | All important entities in the system (defined in the database schema below) shall be tractable – the history of updates is stored, including who performed the update (which User) and when (date and time). |

### Appointment subsystem
_The appointment subsystem is critical for defining the study workflow. Technically, every step that requires a separable work with a participant is an appointment. A study step is usually represented by a real appointment, but it is not necessary; for example, eligibility criteria are determined by a special (empty) appointment._

| ID | Requirement |
| --- | --- |
| F200 | The appointment subsystem shall manage each participant's appointments and define the study workflow (study steps). |
| F210 | _Data perspective:_ The appointment entity shall be composed of appointment type, date and time of creation, a participant (person in participant subsystem), booked date (if applicable), booked location (if applicable), date of visit (if applicable), appointment stage, a flag indicating the eCRF is completed (if applicable), another flag indicating the consent (eCRF) is given (if applicable). |
| F220 | _Functional perspective:_ The appointment type shall define the steps of the study - therefore contains the relative position of appointment (step) among others, indicates whether eCRF (or consent) is required at this appointment, and contains a reference to eCRF (or consent) form (if applicable), has a flag indicating a participant must visit some location (e. g. for collection of samples), contains the name and description of the appointment (study step). |
| F230 | The appointment entity shall be related to event logs that shall store all events that have taken place (like phone calls, emails, actions, and follow-ups) related to the appointment. |
| F240 | Where applicable, the event log shall store and manage notes related to each log (a record). _(For example, the study manager wants to write information about calls that have been taken to organize an appointment, note things like if anything went wrong, e. g. aggressive behaviour of the participant, etc.)_ |
| F250 | The appointment stage shall describe in what phase (status, situation) the appointment is. The values are: contacted, unreachable, want or need more time, declined, finished (indicating that the appointment is closed). |

### Administration subsystem
_The administration subsystem technically describes requirements related to the front-end (how to manage entities effectively) and issues related to the technical (back-end) part._

| ID | Requirement |
| --- | --- |
| F260 | The administration subsystem components shall be related to the actual management of the study. |
| F270 | The administration subsystem shall operate with users (entity User in database schema) in three tires: root (without any limitations, for technical support), research administrator (supervising role), and research assistant (midwives, research nurses). |
| F280 | The administration subsystem shall be accessible only to the user with proper credentials (password-protected part). |
| F290 | The research administrators shall be capable of reviewing research assistants' work, deciding who is eligible for the study and performing statistical queries (TODO). |
| F300 | The research assistants shall be users with the lowest privilege levels. They shall be allowed to manage participants, arrange appointments, log all details related to their work and update each participant's personal information. |
| F310 | The administrator subsystem shall generate notifications about possible new participants and reminders about appointments to users.  |
| F320 | The system shall generate a PDF file (label) with a person ID ready for printing. (This label is for samples - it is about to be printed and stuck on a test tube.) |

#### Views related functionality
_The following represents some fundamental requirements for views in the system. Besides that, all standard requirements for detail views and list views are in place. When defining filters and sorting logic, please follow common sense. And follow the same even when defining details view (to have an as simple interface as possible)._

| ID | Requirement |
| --- | --- |
| F330 | The administrator subsystem shall have a view that lists all participants matching to selected criteria. |
| F340 | Any list of all entities in any view shall have a pagination with a selected number of items per page. |
| F350 | Any list of entities in any view shall support sorting by all applicable columns. |
| F360 | The selectable criteria in the participant view shall be at least: all participants, participants in the selected study step (appointment), and participant matching to searching request (if applicable). |
| F370 | The participant view shall support search by name (or part of the name), NHS number, study ID, and family ID. |
| F380 | The administrator subsystem shall have a view that lists all study steps (appointment definitions) matching selected criteria. |
| F390 | The appointment list view shall support all standard filters and sorting logic. |

## Performance requirements
| ID | Requirement |
| --- | --- |
| P010 | The latency in communication between internal back-end components shall not exceed 0.2 seconds (at probability quantile 0.99). |
| P020 | The latency in communication between front-end clients located in UK and back-end services shall not exceed 1 second (at probability quantile 0.6). |

## Usability requirements
| ID | Requirement |
| --- | --- |
| U010 | The system front-end shall be optimized for mobile usability following ISO 9241 and ISO 25062 standards. |
| U020 | The system front-end shall meet legal requirements for cookie permissions, privacy statements, GDPR, health regulations, and accessibility statements. |

### Accessibility requirements
| ID | Requirement |
| --- | --- |
| U030 | The system front-end shall be optimised for accessibility following the international WCAG 2.1 AA accessibility standard. |

## Interface requirements
| ID | Requirement |
| --- | --- |
| I010 | The system back-end shall implement a RESTful interface. |
| I020 | The system shall use token-based authentication. |
| I030 | The system shall allow secure export (using appropriate transaction protection) of the internal database content into a separate Research environment's databases. |

## Logical database requirements
_The following (Figure 2) represents the overview of database logic._

![CGULL_ERA.png](CGULL_ERA.png)

Figure 2: Simplified ERA model of database.

## Design constraints
| ID | Requirement |
| --- | --- |
| C010 | The system shall operate with user data under constraints defined by GDPR. |
| C020 | The system shall process sensitive data, which requires following strict security standards. |

## Software system attributes
| ID | Requirement |
| --- | --- |
| A010 | The system shall be available 99.5 per cent of the time. |
| A020 | The system back-end shall be available only through encrypted SSL protocol. |
| A030 | The system shall log every log-in attempt. |
| A040 | The system shall perform a regular (restorable) backup of the database content. |

## Supporting information
| ID | Requirement |
| --- | --- |
| S010 | The system shall be a standard web application with a strictly separated back-end and front-end. |
| S020 | The system shall be composed of a public front-end interface, administrator control panel, and RESTful back-end service on a high level. |

# Appendices
## Acronyms and abbreviations
**CRUD:** Create, Read, Update, Delete

**SMS:** Study Management System
