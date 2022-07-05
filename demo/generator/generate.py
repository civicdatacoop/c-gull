import datetime
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from dataclasses import dataclass

from rand_parts import random_participants

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
                r_participants=random_participants(10)
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
         content_file='page_list.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Imported patients"
         ),
    Page(title="Edit participant",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="edit_participant",
         content_file='page_edit_participant.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Edit participant"
         ),
    Page(title="Edit notes",
         keywords=comm_keywords,  # noqa: E501
         description=comm_description,  # noqa: E501
         url="notes",
         content_file='page_notes.html',
         language="en",
         last_mod=datetime.datetime(2022, 1, 1),
         name="Edit notes"
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