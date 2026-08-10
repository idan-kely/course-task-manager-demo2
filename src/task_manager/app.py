"""Small command-line demo for the task manager."""

from .task import Task


def main() :
    """Create a few sample tasks and print them."""
    tasks = [
        Task("Read the Git chapter"),
        Task("Create the first commit"),
        Task("Push the project to GitHub"),
    ]

    tasks[0].mark_complete()

    print("Course tasks")
    print("------------")
    for task in tasks:
        print(task.display())


if __name__ == "__main__":
    main()

