import openai

def learn_topic():
    openai.api_key = input("Enter your OpenAI API key: ")
    topic = input("What do you want to learn? ")
    time_available = int(input("How many hours do you want to spend learning this topic? "))
    experience_level = int(input("On a scale of 1-10, how much experience do you have with this topic? "))

    prompt = f"Please create a study guide for learning about {topic} in {time_available} hours, for someone with {experience_level}/10 experience. This should be broken down into parts, categories, or steps, or whatever makes sense, with each separated by a blank line. That is the only time the response should contain a blank line."

    # Generate a response from the OpenAI GPT API using the user's inputs
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the course overview from the API response
    course_overview = response.choices[0].text.strip()

    print(f"Study Guide:\n{course_overview}\n")

    # Split the GPT response into parts, categories, or steps
    parts = course_overview.split("\n\n")

    file_name = input("Enter a file name to save the output to (without extension): ")

    with open(f"{file_name}.md", "w") as f:
        # Write the topic, time available, and experience level to the file
        f.write(f"# Study Guide for Learning About {topic}\n")
        f.write(f"Time available: {time_available} hours\n")
        f.write(f"Experience level: {experience_level}/10\n\n")

        # Write the course overview to the file
        f.write(f"## Course Overview\n{course_overview}\n\n")

        # Loop through each part and ask the user if they want to learn the next section or ask the GPT API for more information
        for i, part in enumerate(parts):
            print(f"{part}")
            learn_part(part, f)

        print(f"Study guide saved to {file_name}.md")

def learn_part(part, file):
    print(f"Learning...")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Explain or instruct someone who is learning about the following: {part}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the course material from the API response
    course_material = response.choices[0].text.strip()
  
    # Print the course material to the command line
    print(course_material)
  
    # Prompt the user to choose to learn the next section or ask the GPT API for more information
    while True:
        choice = input("Enter 'n' for the next section or 'a' to ask GPT API: ")
        if choice == 'n':
            # Write the course material to the file and return
            file.write(f"{course_material}\n")
            return
        elif choice == 'a':
            # Prompt the user for the additional prompt to ask the GPT API for
            additional_prompt = input("Enter a prompt for the GPT API: ")
            # Get the response from the GPT API using the additional prompt
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=additional_prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            # Extract the course material from the API response
            additional_response = response.choices[0].text.strip()

            # Print the additional response to the command line
            print(additional_response)
          
            # Extract the course material from the API response and write it to the file as a comment
            course_material += f"\n<!-- GPT API response to '{additional_prompt}': -->\n{response.choices[0].text.strip()}\n<!-- End of GPT API response -->\n"
        else:
            # Invalid choice, prompt the user again
            print("Invalid choice, please enter 'n' for the next section or 'a' to ask GPT API.")

if __name__ == '__main__':
    learn_topic()

