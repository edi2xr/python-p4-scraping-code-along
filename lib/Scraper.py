from bs4 import BeautifulSoup
from lib.Course import Course

class Scraper:
    def __init__(self, url=None):
        self.url = url
        self.courses = []

    def get_page(self):
        """Get HTML page either from URL or local mock file."""
        if self.url:
            import requests
            response = requests.get(self.url)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        else:
            # Load local mock HTML file for testing
            with open("mock_courses.html") as f:
                return BeautifulSoup(f, "html.parser")

    def get_courses(self):
        """Return a list of course elements from the page."""
        soup = self.get_page()
        return soup.select(".course")

    def make_courses(self):
        """Create Course instances from the page and store in self.courses."""
        course_elements = self.get_courses()
        for c in course_elements:
            title = c.select_one(".title").text.strip()
            schedule = c.select_one(".schedule").text.strip()
            description = c.select_one(".description").text.strip()
            self.courses.append(Course(title, schedule, description))
        return self.courses
