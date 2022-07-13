import datetime
import random
from random import randrange
from datetime import timedelta


study_phases = [
        'Initial interview',
        'First pre-delivery visit',
        'Second pre-delivery visit',
        'Post dispatch follow-up'
    ]

locations = [
    'Room 423, Liverpool Womens Trust',
    'Room 286, Broadgreen Hospital',
    'Reception, Spire Hospital',
    'Section C, Royal University Hospital'
]

professionals = [
        'Joanna Mills',
        'Peter Johnson',
        'Kale Understone',
        'Hanna Waters'
    ]


def random_date() -> datetime.datetime:
    """
    This function will return a random datetime between two datetime
    objects.
    """
    start = datetime.datetime.strptime('1/1/2020 9:30 AM',
                                       '%m/%d/%Y %I:%M %p')
    end = datetime.datetime.strptime('12/31/2022 06:30 PM',
                                     '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def random_address() -> str:
    addresses = ['66 Victoria Road, DUMFRIES, DG50 2TU',
                 '10 Richmond Road, BLACKPOOL, FY41 9HR',
                 '20 Station Road, REDHILL, RH83 8JN',
                 '62 Green Lane, LUTON, LU4 8IY',
                 '56 Manor Road, KIRKCALDY, KY90 6NL',
                 '93 Alexander Road, SUTTON, SM98 9LH']
    return random.choice(addresses)


def random_participants(count: int = 10,
                        email_provider: str = "gmail.com") -> list[dict]:
    first_names = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia']
    middle_names = ['Isabella', 'Mia', 'Evelyn', 'Harper', 'Flora', 'Raya']
    last_names = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Davies']
    study_numbers = ['A8J93K4L', 'C3WA3QC1', 'K8D2EQ3C', 'P9K4NS9A', 'D3HLD8LE']
    sources = ['K2', 'Volunteer']
    nhs_numbers = ['6442981355', '1395213089', '1678898600', '4600844858', '6690273245']
    is_participant = ['No', 'Yes', 'Pending']
    action_required = ['No', 'Yes']
    languages = ['English', 'Spanish', 'Italian']

    participant = []
    for pos in range(count):
        created = random_date().strftime("%Y/%m/%d %H:%M")
        phone = "(0)" + str(random.randint(1000000000, 9999999999))
        s_f_name = random.choice(first_names)
        s_l_name = random.choice(last_names)
        email = f"{s_f_name}.{s_f_name}@{email_provider}".lower()
        dob = f"{random.randint(1970, 1999)}/" \
              f"{random.randint(1, 12)}/" \
              f"{random.randint(13, 28)}"
        participant.append(
            {
                "position": pos + 1,
                "created": created,
                "phone": phone,
                "first_name": s_f_name,
                "last_name": s_l_name,
                "middle_name": random.choice(middle_names),
                "email": email,
                "dob": dob,
                "study_number": random.choice(study_numbers),
                "source": random.choice(sources),
                "nhs_number": random.choice(nhs_numbers),
                "is_participant": random.choice(is_participant),
                "action_required": random.choice(action_required),
                "language": random.choice(languages),
                "address": random_address()
            }
        )
    return participant


def random_person_appointments(count: int = 10) -> list[dict]:

    appointment_stages = [
        'created',
        'contacted',
        'unreachable',
        'want / need more time'
        'declined',
        'finished'
    ]
    ecrf_states = ['required', 'passed', 'rejected', 'no']
    apps = []
    for pos in range(count):
        apps.append({
            'position': pos + 1,
            'study_phase': random.choice(study_phases),
            'created_on': random_date().strftime("%Y/%m/%d %H:%M"),
            'author': random.choice(professionals),
            'booked_on': random.choice(
                ["N/A", random_date().strftime("%Y/%m/%d %H:%M")]
            ),
            'visited_on': random.choice(
                ["N/A", random_date().strftime("%Y/%m/%d %H:%M")]
            ),
            'location': random.choice(locations),
            'ecrf': random.choice(ecrf_states),
            'appointment_stage': random.choice(appointment_stages),
            'action_required': random.choice(['yes', 'no']),
            'events_logged': random.choice(['yes', 'no']),
            'notes': random.randint(0, 3),
        })

    return apps


def random_study_phases(count: int = 10) -> list[dict]:
    required_options = ['Voluntary', 'Compulsory']
    ecrf_cons = ['eCRF form', 'Consent', 'Neither']
    yes_no = ['yes', 'no']
    phases = []
    for pos in range(count):
        phases.append({
            'position': pos + 1,
            'phase_name': random.choice(study_phases),
            'relative_position': random.choice(['N/A', random.randint(1, 10)]),
            'required': random.choice(required_options),
            'ecrf_consent': random.choice(ecrf_cons),
            'in_person': random.choice(yes_no),
            'samples_collection': random.choice(yes_no),
            'number_of_participants': random.randint(0, 30000),
        })
    return phases


def random_locations(count: int = 10) -> list[dict]:
    locations_pool = []
    comments = ['From July Ward C, till then Ward A',
                'Closed on Sunday and Monday',
                'No longer than 10 minutes appointments']
    for pos in range(count):
        locations_pool.append({
            'position': pos + 1,
            'location_name': random.choice(locations),
            'address': random_address(),
            'comment': random.choice(comments),
            'created_on': random_date().strftime("%Y/%m/%d %H:%M")

        })
    return locations_pool


def random_itinerary(count: int = 10) -> list[dict]:
    participants = random_participants(count)
    itinerary: list = []
    for position, participant in enumerate(participants):
        itinerary.append({
            'position': position + 1,
            'appointment': random_date().strftime("%Y/%m/%d %H:%M"),
            'last_name': participant['last_name'],
            'first_name': participant['first_name'],
            'study_number': participant['study_number'],
            'location': random.choice(locations),
            'phone': participant['phone'],
            'email': participant['email'],
            'address': participant['address'],
            'language': participant['language']
        })
    return itinerary


def random_users(count: int = 10) -> list[dict]:
    privileges = ['root', 'study administrator', 'research assistant',
                  'secretary']
    employers = ['Womens Hospital Trust', 'NHS', 'Liverpool Hospital']
    job_titles = ['Leading Nurse', 'Nurse', 'University researcher', 'Midwife']
    people = random_participants(count, 'nhs.co.uk')
    users = []
    for pos, person in enumerate(people):
        users.append({
            **person,
            'privilege': random.choice(privileges),
            'employer': random.choice(employers),
            'job_title': random.choice(job_titles),
            'employee_id': random.randint(10_000_000, 99_999_999),
            'password_expire': random.randint(5, 120),
            'created_by': random.choice(professionals),
            'comment': random.choice(['N/A', 'Some comment'])
        })

    return users
