import logging

from mkdocs.plugins import event_priority
from mkdocs.structure.nav import Section

log = logging.getLogger("mkdocs.plugins.blog_nav")


@event_priority(-50)
def on_nav(nav, config, files):
    # get all the Post objects out of the files collection
    posts_pages = [
        f.page
        for f in files
        if f.is_documentation_page() and f.page and type(f.page).__name__ == "Post"
    ]

    # sort reverse chronologically
    try:
        posts_pages.sort(key=lambda p: p.meta.get("date"), reverse=True)
    except Exception as e:
        log.warning(f"Failed to sort some blog posts by date: {e}")

    # construct the "posts" sidebar section
    if posts_pages:
        posts_section = Section(title="posts", children=posts_pages)
        nav.items.append(posts_section)
        log.info(f"Successfully added 'posts' section with {len(posts_pages)} posts.")

    return nav
