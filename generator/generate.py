import datetime
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from dataclasses import dataclass

from rand_parts import random_participants, random_person_appointments, \
    random_study_phases, random_locations, random_itinerary, random_users

# Path to TEMPLATES folder (relative to where you run the script)
PATH_TO_TEMPLATES = Path('../generator/TEMPLATES/')
# Path to RESOURCES folder (relative to where you run the script)
PATH_TO_RESOURCES = Path('../generator/RESOURCES/')
# Path to output folder (relative to where you run the script)
PATH_TO_OUTPUT = Path('../docs/')
# Root URL
URL_ROOT = "https://civicdatacooperative.com/"

# Link to homepage
link_to_homepage = "index.html"  # TODO: always '/' in production
# File suffix
html_file_suffix = ".html"


@dataclass()
class Page(object):
    title: str
    keywords: str
    description: str
    content_file: str
    url: str
    language: str
    last_mod: datetime.datetime
    name: str

    def keys(self):
        """Get keys that allows conversion of this class to dictionary.
        Returns:
            List[str]: List of the keys to be passed to template.
        """
        return ['title', 'keywords', 'description', 'url', 'content_file',
                'language', 'name']

    def __getitem__(self, key):
        """Allows conversion of this class to dictionary.
        """
        return getattr(self, key)

    def generate_site(self):
        with open(PATH_TO_TEMPLATES.joinpath('page.html')) as tem_han:
            template = Environment(
                loader=FileSystemLoader(PATH_TO_TEMPLATES)
            ).from_string(tem_han.read())
            html_str = template.render(
                **dict(self),
                link_to_homepage=link_to_homepage,
                r_participants=random_participants(10),
                r_person_appointments=random_person_appointments(10),
                r_study_phases=random_study_phases(10),
                r_locations=random_locations(10),
                r_itinerary=random_itinerary(10),
                r_users=random_users(10)
            )
            return html_str

    @property
    def absolute_url(self):
        if self.url != 'index':
            return URL_ROOT + self.url + html_file_suffix
        return URL_ROOT

    @property
    def last_modified(self):
        if self.last_mod is None:
            return None
        return self.last_mod.strftime('%Y-%m-%d')


# Common meta tags
comm_keywords: str = "Test"
comm_description: str = "CIPHA."  # noqa: E501


# Pages definition
pages = [
    Page(title="Imported patients",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="index",
         content_file='page_person_list.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Imported patients"
         ),
    Page(title="Edit participant",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="edit_participant",
         content_file='page_person_detail.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Edit participant"
         ),
    Page(title="Edit notes",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="notes",
         content_file='page_person_notes.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Edit notes"
         ),
    Page(title="Person's appointments",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="person_appointment",
         content_file='page_person_appointment_list.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Person's appointments"
         ),
    Page(title="Person's appointment editor",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="edit_person_appointment",
         content_file='page_person_appointment_detail.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Appointment editor"
         ),
    Page(title="Withdraw participant",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="withdraw",
         content_file='page_withdraw.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Withdraw participant"
         ),
    Page(title="Study phases",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="study_phases",
         content_file='page_study_phases.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Study phases"
         ),
    Page(title="New study phase",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="new_phase",
         content_file='page_new_phase.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="New study phase"
         ),
    Page(title="Locations",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="locations",
         content_file='page_locations.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Site Locations"
         ),
    Page(title="Edit location",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="edit_location",
         content_file='page_edit_location.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Site Location"
         ),
    Page(title="Edit person's eligibility",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="person_eligibility",
         content_file='page_person_eligibility.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Person's eligibility"
         ),
    Page(title="Edit person's relations",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="person_relations",
         content_file='page_person_relations.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Person's relations"
         ),
    Page(title="Study itinerary",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="itinerary",
         content_file='page_itinerary_list.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Study itinerary"
         ),
    Page(title="Users in system",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="users",
         content_file='page_user_list.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Users in system"
         ),
    Page(title="New user",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="add_user",
         content_file='page_user_detail.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="New user"
         ),
]

# Remove all existing resources
if PATH_TO_OUTPUT.exists():
    shutil.rmtree(PATH_TO_OUTPUT)

# Create new dir
PATH_TO_OUTPUT.mkdir()

for page in pages:
    content = page.generate_site()
    with PATH_TO_OUTPUT.joinpath(page.url + html_file_suffix).open('w', encoding="utf-8") as fp:
        fp.write(content)

# Copy resources
shutil.copytree(PATH_TO_RESOURCES, PATH_TO_OUTPUT, dirs_exist_ok=True)

# Generate site map (XML):
with open(PATH_TO_TEMPLATES.joinpath('site_map.xml')) as tem_han:
    template = Environment(
        loader=FileSystemLoader(PATH_TO_TEMPLATES)
    ).from_string(tem_han.read())
    html_str = template.render(
        sites=pages
    )
    with PATH_TO_OUTPUT.joinpath('sitemap.xml').open('w') as f_xml:
        f_xml.write(html_str)

# Generate robots.txt file
robots_txt_content = f"""User-agent: *
Allow: /
Sitemap: {URL_ROOT}sitemap.xml"""
with PATH_TO_OUTPUT.joinpath('robots.txt').open('w') as robots_txt_h:
    robots_txt_h.write(robots_txt_content)
