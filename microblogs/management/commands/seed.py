from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):
    def _init_(self):
        super(),_init_()
        self.faker = Faker('en_GB')
        for i in range (100):
            i = User.objects.create_user(
                '@' + faker.user_name,
                first_name = faker.first_name(),
                last_name = faker.last_name(),
                email = faker.email(),
                password = faker.password(),
                bio = faker.bio()
            )

    def handle(self, *args, **options):

        print("WARNING: The SEED command has not been implemented yet.")
