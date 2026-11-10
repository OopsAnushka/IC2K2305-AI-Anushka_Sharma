
# Lab 4: Knowledge Representation and Logical Reasoning

# 1. Predicate Representation
print("1. PREDICATE REPRESENTATION")

facts = [
    ("student", "Anushka"),
    ("studies", "Anushka", "Artificial Intelligence"),
    ("has_topic", "Artificial Intelligence", "Machine Learning"),
    ("has_topic", "Artificial Intelligence", "Knowledge Representation")
]

for fact in facts:
    print(fact)


# 2. Logical Inference
print("\n2. LOGICAL INFERENCE")

inferred_facts = []

for fact in facts:
    if fact[0] == "studies":
        person = fact[1]
        subject = fact[2]

        for topic_fact in facts:
            if topic_fact[0] == "has_topic":
                if topic_fact[1] == subject:
                    new_fact = ("learns", person, topic_fact[2])
                    inferred_facts.append(new_fact)

print("Inferred Facts:")
for fact in inferred_facts:
    print(fact)


# 3. Semantic Network
print("\n3. SEMANTIC NETWORK")

semantic_network = {
    "Anushka": {
        "is_a": "Student",
        "studies": "Artificial Intelligence"
    },
    "Artificial Intelligence": {
        "is_a": "Subject",
        "has_topic": ["Machine Learning",
                      "Knowledge Representation"]
    }
}

for node, relations in semantic_network.items():
    print(node, "->", relations)


# 4. Frame Representation
print("\n4. FRAME REPRESENTATION")

student_frame = {
    "Frame_Name": "Student",
    "Name": "Anushka",
    "Course": "B.Tech",
    "Subject": "Artificial Intelligence",
    "Year": "Third Year"
}

for key, value in student_frame.items():
    print(key, ":", value)


# 5. Conceptual Dependency
print("\n5. CONCEPTUAL DEPENDENCY")

action = {
    "Actor": "Anushka",
    "Action": "TRANSFER",
    "Object": "Book",
    "From": "Library",
    "To": "Classroom"
}

for key, value in action.items():
    print(key, ":", value)


# 6. Rule-Based System
print("\n6. RULE-BASED SYSTEM")

temperature = 32
person_present = True

if temperature > 30 and person_present:
    print("Rule: IF temperature > 30 AND person is present")
    print("THEN switch on the fan")
    print("Decision: Fan switched ON")

else:
    print("Decision: Fan remains OFF")


print("\nAll experiments completed successfully!")
