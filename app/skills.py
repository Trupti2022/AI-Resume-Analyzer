SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "React",
    "Angular",
    "Node.js",
    "NestJS",

    "REST API",
    "GraphQL",
    "Webhooks",
    "OAuth 2.0",

    "CRM",
    "HubSpot",

    "CI/CD",
    "Jenkins",
    "GitLab",

    "Kafka",
    "RabbitMQ",

    "Docker",
    "Kubernetes",

    "AWS",
    "Azure",

    "MongoDB",
    "PostgreSQL",
    "MySQL",

    "Terraform",

    "Event Driven Architecture",
    "Microservices",

    "Power BI",
    "Machine Learning",

    "Agile",
    "Scrum"
]

def extract_skills(text):

    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills