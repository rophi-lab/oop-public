"""
Exercise 21.5c: Factory Method

Goal:
    ReportApp.generate() is already written. It does two things:
        report = self.create_report()
        return report.render(title)
    A subclass decides which report object to create.
    Do not edit Report or ReportApp.

--------------------------------------------------------------------------------
Write the four methods below. Each one is a single return.

1. PlainReport.render(self, title)
    Return title with no extra characters.
    "Results" stays "Results".

2. MarkdownReport.render(self, title)
    Return a level-1 Markdown heading.
    Put "# " in front of the title. There is one space after the hash.
        return "# " + title
    "Results" becomes "# Results".

3. PlainApp.create_report(self)
    This is the factory method for plain text.
    Return a new PlainReport object:
        return PlainReport()
    Do not call render() here. generate() does that.

4. MarkdownApp.create_report(self)
    Return a new MarkdownReport object:
        return MarkdownReport()

How the demo uses your code:
    PlainApp().generate("Results")
        -> PlainApp.create_report() returns a PlainReport
        -> that report's render("Results") returns "Results"

    MarkdownApp().generate("Results")
        -> MarkdownApp.create_report() returns a MarkdownReport
        -> that report's render("Results") returns "# Results"

How to run:
    python main.py
"""


class Report:
    def render(self, title: str) -> str:
        raise NotImplementedError


class PlainReport(Report):
    def render(self, title: str) -> str:
        # TODO: return title unchanged.
        pass


class MarkdownReport(Report):
    def render(self, title: str) -> str:
        # TODO: return "# " + title
        #       "Results" -> "# Results"
        pass


class ReportApp:
    """Shared workflow. Do not change this class."""

    def create_report(self) -> Report:
        raise NotImplementedError

    def generate(self, title: str) -> str:
        report = self.create_report()
        return report.render(title)


class PlainApp(ReportApp):
    def create_report(self) -> Report:
        # TODO: return PlainReport()
        #       Do not call render() here.
        pass


class MarkdownApp(ReportApp):
    def create_report(self) -> Report:
        # TODO: return MarkdownReport()
        pass


# ------------------------------- DO NOT EDIT -------------------------------- #

if __name__ == "__main__":
    print(PlainApp().generate("Results"))
    print(MarkdownApp().generate("Results"))


# Expected Output:
# Results
# # Results
