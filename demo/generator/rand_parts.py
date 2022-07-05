import datetime
import random

def random_address() -> str:
    addresses = ['66 Victoria Road, DUMFRIES, DG50 2TU',
                 '10 Richmond Road, BLACKPOOL, FY41 9HR',
                 '20 Station Road, REDHILL, RH83 8JN',
                 '62 Green Lane, LUTON, LU4 8IY',
                 '56 Manor Road, KIRKCALDY, KY90 6NL',
                 '93 Alexander Road, SUTTON, SM98 9LH']
    return random.choice(addresses)

def random_participants(count: int = 10) -> list[dict]:
    first_names = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia']
    middle_names = ['Isabella', 'Mia', 'Evelyn', 'Harper', 'Flora', 'Raya']
    last_names = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Davies']
    study_numbers = ['A8J93K4L', 'C3WA3QC1', 'K8D2EQ3C', 'P9K4NS9A', 'D3HLD8LE']
    sources = ['K2', 'Volunteer']
    nhs_numbers = ['6442981355', '1395213089', '1678898600', '4600844858', '6690273245']
    enrolleds = ['No', 'Yes']
    contacteds = ['No', 'Yes']
    languages = ['English', 'Spanish', 'Italian']

    participant = []
    for pos in range(count):
        created = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        phone = "(0)" + str(random.randint(1000000000, 9999999999))
        s_f_name = random.choice(first_names)
        s_l_name = random.choice(last_names)
        email = f"{s_f_name}.{s_f_name}@out.com".lower()
        dob = f"{random.randint(1970, 1999)}/" \
              f"{random.randint(1, 12)}/" \
              f"{random.randint(13, 28)}"
        participant.append(
            {
                "position": pos + 1,
                "created": created,
                "phone": phone,
                "first_name": s_f_name,
                "last_name": s_l_name,
                "middle_name": random.choice(middle_names),
                "email": email,
                "dob": dob,
                "study_number": random.choice(study_numbers),
                "source": random.choice(sources),
                "nhs_number": random.choice(nhs_numbers),
                "enrolled": random.choice(enrolleds),
                "contacted": random.choice(contacteds),
                "language": random.choice(languages),
                "address": random_address()
            }
        )
    return participant
