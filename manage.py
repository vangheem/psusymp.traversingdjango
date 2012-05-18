from django.core.management import execute_manager
from psusymp.traversingdjango import settings

if __name__ == "__main__":
    execute_manager(settings)
