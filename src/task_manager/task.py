"""Task model used by the course task manager."""

class Task:
    """A single task in the course."""
    def __init__(self, title, completed):
        self.title = title
        self.completed = completed

    def mark_complete(self) :
        """Mark the task as completed."""
        self.completed = True

    def display(self):
        """Return a short, user-friendly representation."""
        status = "x" if self.completed else " "
        return f"[{status}] {self.title}"

