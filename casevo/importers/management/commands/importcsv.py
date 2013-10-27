from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Import a csv file containing transactions."
    args = "<filename>"

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError("Please provide a filename.")

        filename = args[0]

        print filename
