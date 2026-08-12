import os

from splent_framework.seeders.BaseSeeder import BaseSeeder

from splent_io.splent_feature_about.models import AboutSection

try:
    from splent_io.splent_feature_media.services import MediaService
except ImportError:
    MediaService = None


def _seed_image(filename, title=""):
    """Import a bundled photo through the media feature and return its public URL.

    Returns "" when the media feature is not installed so callers can simply
    drop the image.
    """
    if MediaService is None:
        return ""
    path = os.path.join(os.path.dirname(__file__), "seed_media", filename)
    item = MediaService().import_from_file(
        path, title=title, source_key="seed://about/" + filename
    )
    return item.url


# Content migrated from diversolab.us.es: the "About Us" page (id 11) plus the
# homepage intro blurb, and the "Our values" page (English version, id 3019),
# with the Elementor markup cleaned down to semantic HTML.

# Photos bundled in seed_media/, shown between the two subsections, in order.
WHO_WE_ARE_IMAGES = [
    ("university-of-seville.jpg", "University of Seville"),
    (
        "computer-engineering-school-seville.jpg",
        "School of Computer Engineering, University of Seville",
    ),
]

WHO_WE_ARE = """\
<p>We specialize in variability-intensive systems, focusing on all aspects of
variability. We have pioneered automated analysis techniques globally to
address these systems, as well as systems and software product lines. Our
expertise spans cybersecurity, data visualization, video encoding, mobile
computing, web development, FLOSS management, DevOps, software testing,
software evolution, and software architecture, among other areas.</p>

<h3>Historical background</h3>
<p>The Diverso Lab was initiated in 2012 with the starting of Jose A.
Galindo's PhD thesis advised by David Benavides. In that time, Jose A. had
difficulties to study a PhD thesis in Sevilla and we found a Talentia
competitive scholarship, so he did his PhD in a co-tutelle programme with
Virginia Tech, INRIA Rennes and University of Seville involved. In
perspective, this was the birth of the DiversoLab. We have always had an
international and collaborative perspective. We belong to the
<a href="https://i3us.us.es/">I3US institute on informatics</a>.</p>

{images}

<h3>Research fields</h3>
<p>We are specialized in variability-intensive systems. Everything that has
variability is of our interest. We have pioneered worldwide automated
analysis techniques to deal with variability-intensive systems and systems
and software product lines. Some of the areas where we applied those
techniques are Artificial Intelligence, Cybersecurity, Health, Agriculture,
Education, Computational Thinking, Data Visualization, Video Encoding,
Mobile Computing, Web Development, FLOSS management, DevOps, Software
Testing, Software Evolution and Software Architecture, among many others.</p>
"""

OUR_VALUES = """\
<p>At Diverso Lab our motto is "international computing", an expression that
reflects our international and collaborative calling in science and
innovation. But that global outlook always stems from a clear commitment, to
work for our land and contribute to the progress and wellbeing of
Andalusia.</p>

<p>From our research group at the University of Seville, one of our core
values is to advance knowledge in software engineering, artificial
intelligence, and computer systems in general, strategic fields for the
technological, social, and economic development of the community closest to
us. In a context like the present one, shaped in 2025 and 2026 by the
consolidation of generative artificial intelligence, the new European AI
regulation, and the push toward digital technological sovereignty, our role
as active agents of innovation is highly relevant.</p>

<p>Andalusia is living through a pivotal moment in its digital
transformation. Technology is no longer merely a support, but an essential
infrastructure for competitiveness and social cohesion. In this scenario, we
work on developing high-quality, innovative software and on implementing
intelligent systems that optimize processes in sectors such as health,
education, industry, public administration, and agriculture. The responsible
integration of emerging technologies, such as artificial intelligence, the
Internet of Things, and data-based systems, is part of our day-to-day work,
always from an ethical, critical, sustainable, and people-centered
perspective.</p>

<p>Our research seeks not only to solve technical challenges, but to
contribute to an Andalusia that is fairer, more inclusive, sustainable,
equal, and prepared for global challenges. We believe that the digital
future is built with local talent, international cooperation, and a genuine
commitment to what is close to home.</p>

<p>We believe in the common good and in solidarity, as we see it as a more
efficient and productive way of building for the long term, and that is why
we define a series of values, which are the following.</p>

<ul>
<li>Excellence, understood as rigor and continuous improvement. We shy away
from elitist, exclusionary, or sectarian declarations of excellence. We
believe in work done well, with effort, rigor, self-criticism, and
continuous improvement. We recognize all the talent around us and, although
we are aware of the economic and social constraints of our environment, we
want to help change it through quality.</li>
<li>Solidarity. We set ourselves the goal of dedicating 0.7% of our budget
to development aid, solidarity, and cooperation. We believe in solidarity
outward but also inward. We prefer cooperation to competition.</li>
<li>Equality as a pillar of our action. Equality from many perspectives,
including the promotion and participation of women and men on equal terms,
striving to bring female talent into a male-dominated profession such as
computer engineering.</li>
<li>Sustainability as an element of climate and environmental awareness. We
are aware of the planet's limits and strive to promote sustainable projects
with an eco-logical conscience.</li>
<li>Technological sovereignty as a structuring element of balanced powers in
the management of information and technology. Wherever we can, we commit to
free, decentralized, and collaborative systems.</li>
<li>Defense of the public services system, with special attention to public
health and education. We believe that everyone has the right to quality
public services, and to that end we work to strengthen the public services
network, with special attention to health and education. We believe that
resources and projects should be devoted to strengthening collaboration with
public service entities, with particular emphasis on the public health and
education systems.</li>
<li>Defense of peace and non-violence. We believe that the best way to
resolve conflicts is through peace, dialogue, and non-violence. We believe
that resources and projects should be devoted to projects of peace and
progress, prioritizing other types of projects over defense or military
ones.</li>
<li>A secular education and research that, while respecting individual
beliefs, is entirely independent of any religious doctrine. It is grounded
strictly in reason, critical thinking, and scientific knowledge,
safeguarding freedom of conscience, tolerance, and respect for diversity
without imposing dogmas.</li>
<li>A transparent mode of operation, in which group members and even
outsiders can know our values and our decision-making process. With
traceable decisions and identifiable people responsible for them.</li>
<li>A collaborative and ethical decision-making system. Collaborative, in
which decision-making power is shared and reached by consensus. We believe
that more collaborative decisions are generally better.</li>
<li>An international vision of education and research that is compatible
with recognizing and valuing the local as well, one that is curious about
what is diverse, tolerant of differences, and marked by a multicultural
outlook.</li>
<li>We value collaboration with industry as an opportunity to transfer
knowledge from the university to society, and vice versa, but collaborations
with private companies must guarantee that the group can publish results
openly or reuse them for other research.</li>
<li>We believe in open science, so we give priority to projects,
conferences, journals, and initiatives in which we can publish our results,
tools, and datasets under free licenses that allow their reuse by society
and reproducibility by the research community.</li>
<li>We believe our work is complete when the results genuinely reach
society. Therefore, we are not satisfied with merely publishing an article;
afterward we organize outreach, dissemination, and transfer activities to
bring the results of our work to the people, communities, and institutions
involved.</li>
<li>We prioritize the physical and mental health of our team members, and of
our collaborators, above any of the objectives listed above.</li>
</ul>
"""


def _who_we_are_images_html():
    tags = []
    for filename, alt in WHO_WE_ARE_IMAGES:
        url = _seed_image(filename, title=alt)
        if url:
            tags.append(f'<img src="{url}" alt="{alt}">')
    return "\n".join(tags)


class AboutSeeder(BaseSeeder):
    def run(self):
        self.seed(
            [
                AboutSection(
                    slug="who-we-are",
                    title="Who we are",
                    content=WHO_WE_ARE.format(images=_who_we_are_images_html()).strip(),
                    order=1,
                    published=True,
                ),
                AboutSection(
                    slug="our-values",
                    title="Our values",
                    content=OUR_VALUES.strip(),
                    order=2,
                    published=True,
                ),
            ]
        )
