import ast
import operator
import random


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def calculate_expression(expression):
    node = ast.parse(expression, mode="eval").body

    def evaluate(current_node):
        if isinstance(current_node, ast.Constant) and isinstance(current_node.value, (int, float)):
            return current_node.value

        if isinstance(current_node, ast.BinOp) and type(current_node.op) in OPERATORS:
            left = evaluate(current_node.left)
            right = evaluate(current_node.right)
            return OPERATORS[type(current_node.op)](left, right)

        if isinstance(current_node, ast.UnaryOp) and type(current_node.op) in OPERATORS:
            return OPERATORS[type(current_node.op)](evaluate(current_node.operand))

        raise ValueError("Unsupported expression")

    return evaluate(node)


def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "howdy", "sup", "what's up", "whats up", "yo"]:
        return random.choice([
            "Hello! How can I help you today?",
            "Hey there! What's on your mind?",
            "Hi! Great to see you. How can I assist?",
        ])

    # How are you
    elif user_input in ["how are you", "how are you doing", "how's it going", "how do you do"]:
        return "I'm doing great, thanks for asking! How about you?"

    # User says they are good
    elif user_input in ["i'm good", "im good", "i'm fine", "im fine", "good", "fine", "great", "not bad"]:
        return "Glad to hear that! Is there anything I can help you with?"

    # User says they are bad
    elif user_input in ["i'm sad", "im sad", "not good", "bad", "terrible", "awful", "not great"]:
        return "I'm sorry to hear that. I hope things get better for you soon! Remember, tough times don't last."

    # User is bored
    elif "bored" in user_input:
        return random.choice([
            "Bored? Ask me for a joke, a fun fact, or a riddle!",
            "Why not learn something new today? Ask me a fun fact!",
            "Try asking me for a riddle or a random hobby idea!",
        ])

    # Name
    elif user_input in ["what is your name", "what's your name", "who are you", "your name"]:
        return "I'm ChatBot, your friendly rule-based assistant!"

    # Age
    elif "how old are you" in user_input or "your age" in user_input:
        return "I was just created, so I'm pretty new! Age is just a number for a bot like me."

    # Help
    elif user_input in ["what can you do", "help", "what do you do", "commands", "options"]:
        return (
            "Here are some things you can ask me about:\n"
            "  - Greetings & mood\n"
            "  - Jokes & riddles\n"
            "  - Fun facts & trivia\n"
            "  - Math (e.g. 'what is 5 + 3')\n"
            "  - Advice & motivation\n"
            "  - Movies, music, books, food\n"
            "  - Sports & fitness\n"
            "  - Science, space & nature\n"
            "  - History & geography\n"
            "  - Animals & pets\n"
            "  - Technology & programming\n"
            "  - Travel & languages\n"
            "  - Hobbies & creativity\n"
            "  - Career & money\n"
            "  - Health & sleep\n"
            "  - Relationships & friendship\n"
            "  - Time & weather\n"
        )

    # Exit
    elif user_input in ["bye", "goodbye", "exit", "quit", "see you", "see ya", "later"]:
        return "Goodbye! Have a wonderful day! Come back anytime."

    # Jokes
    elif "joke" in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "What do you call a fake noodle? An impasta!",
            "Why can't your nose be 12 inches long? Because then it would be a foot!",
            "What did the ocean say to the beach? Nothing, it just waved!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "Why did the math book look so sad? Because it had too many problems!",
        ]
        return random.choice(jokes)

    # Riddles
    elif "riddle" in user_input:
        riddles = [
            "I have cities, but no houses live there. I have mountains, but no trees grow there. What am I? (A map!)",
            "The more you take, the more you leave behind. What am I? (Footsteps!)",
            "I speak without a mouth and hear without ears. What am I? (An echo!)",
            "What has hands but can't clap? (A clock!)",
            "What gets wetter the more it dries? (A towel!)",
            "I have keys but no locks. I have space but no room. What am I? (A keyboard!)",
        ]
        return random.choice(riddles)

    # Trivia
    elif "trivia" in user_input:
        trivia = [
            "The Great Wall of China is NOT visible from space with the naked eye — that's a popular myth!",
            "Shakespeare invented over 1,700 words we still use today, including 'bedroom' and 'lonely'.",
            "The human brain generates about 20 watts of power — enough to power a dim light bulb!",
            "There are more possible chess game combinations than atoms in the observable universe.",
            "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid.",
            "A jiffy is an actual unit of time — it's 1/100th of a second!",
        ]
        return random.choice(trivia)

    # Fun facts
    elif "fact" in user_input or "fun fact" in user_input:
        facts = [
            "Honey never spoils. Archaeologists have found 3000-year-old honey in Egyptian tombs!",
            "A group of flamingos is called a flamboyance.",
            "Bananas are technically berries, but strawberries are not.",
            "Octopuses have three hearts and blue blood.",
            "The Eiffel Tower grows about 6 inches taller in summer due to heat expansion.",
            "A day on Venus is longer than a year on Venus.",
            "Crows can recognize and remember human faces.",
            "The average person walks about 100,000 miles in their lifetime.",
        ]
        return random.choice(facts)

    # Motivation
    elif "motivat" in user_input or "inspire" in user_input or "encouragement" in user_input:
        quotes = [
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "It does not matter how slowly you go as long as you do not stop. - Confucius",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "You are capable of more than you know!",
            "Dream big, start small, but most of all — start!",
            "Every expert was once a beginner. Keep going!",
        ]
        return random.choice(quotes)

    # Advice
    elif "advice" in user_input:
        advice = [
            "Take things one step at a time. Progress is progress, no matter how small!",
            "Don't be afraid to ask for help — even the best need support.",
            "Sleep well, eat well, and stay curious. That's a good recipe for life!",
            "Focus on what you can control and let go of what you can't.",
            "Consistency beats perfection. Show up every day and you'll get there.",
        ]
        return random.choice(advice)

    # Math
    elif "what is" in user_input and any(op in user_input for op in ["+", "-", "*", "/"]):
        try:
            expression = user_input.replace("what is", "").strip().rstrip("?")
            result = calculate_expression(expression)
            return f"The answer is {result}!"
        except Exception:
            return "I couldn't calculate that. Try a simple expression like 'what is 5 + 3'."

    # Weather
    elif "weather" in user_input:
        return "I don't have live weather data, but you can check weather.com or your phone's weather app!"

    # Time
    elif "time" in user_input:
        return "I don't have a clock built in, but your device can tell you the current time!"

    # Date
    elif "date" in user_input or "today" in user_input:
        return "I don't have calendar access, but your device's clock should show today's date!"

    # Movies
    elif "movie" in user_input or "film" in user_input:
        return random.choice([
            "I'd recommend 'Inception' if you enjoy mind-bending thrillers!",
            "If you like animation, 'Spider-Man: Into the Spider-Verse' is fantastic!",
            "For a classic, you can't go wrong with 'The Shawshank Redemption'.",
            "If you love sci-fi, 'Interstellar' is breathtaking!",
            "'The Lion King' is a timeless classic for all ages!",
        ])

    # Music
    elif "music" in user_input or "song" in user_input:
        return random.choice([
            "Music is great for the soul! Do you have a favorite genre?",
            "I'd suggest exploring lo-fi music if you need to focus or relax.",
            "Some classics never get old — what kind of music do you enjoy?",
            "Listening to music while working can boost productivity!",
        ])

    # Books
    elif "book" in user_input:
        return random.choice([
            "If you enjoy fiction, try '1984' by George Orwell — a timeless classic!",
            "'The Alchemist' by Paulo Coelho is a wonderful and inspiring read.",
            "For self-improvement, 'Atomic Habits' by James Clear is highly recommended!",
            "'Sapiens' by Yuval Noah Harari is a fascinating read about human history.",
            "If you love mystery, try anything by Agatha Christie!",
        ])

    # Food
    elif "food" in user_input or "eat" in user_input or "hungry" in user_input or "recipe" in user_input:
        return random.choice([
            "I can't eat, but I hear pizza is universally loved!",
            "Feeling hungry? A good meal can fix almost anything!",
            "How about trying a new recipe today? Cooking can be really fun!",
            "Did you know sushi originally meant 'sour-tasting'? The rice was fermented!",
            "Smoothies are a quick and healthy option if you're in a rush!",
        ])

    # Sports
    elif "sport" in user_input or "football" in user_input or "basketball" in user_input or "soccer" in user_input or "cricket" in user_input or "tennis" in user_input:
        return random.choice([
            "Sports are a great way to stay active and have fun!",
            "Do you have a favorite team or sport you follow?",
            "Exercise and sport are great for both body and mind!",
            "The Olympics bring together athletes from every corner of the world — truly inspiring!",
        ])

    # Fitness & health
    elif "fitness" in user_input or "workout" in user_input or "exercise" in user_input or "gym" in user_input:
        return random.choice([
            "Even a 20-minute walk a day can make a big difference to your health!",
            "Consistency is the key to fitness — small efforts add up over time.",
            "Remember to warm up before exercising and cool down after!",
            "Drinking enough water is one of the simplest things you can do for your health.",
        ])

    # Sleep
    elif "sleep" in user_input or "tired" in user_input or "rest" in user_input:
        return random.choice([
            "Sleep is super important! Most adults need 7-9 hours per night.",
            "Feeling tired? A short 20-minute nap can do wonders for your energy!",
            "Try to stick to a consistent sleep schedule — your body will thank you!",
            "Avoid screens before bed to improve your sleep quality.",
        ])

    # Health & mental health
    elif "stress" in user_input or "anxiety" in user_input or "mental health" in user_input:
        return random.choice([
            "It's okay to feel stressed sometimes. Try deep breathing or a short walk to reset.",
            "Mental health is just as important as physical health. Be kind to yourself!",
            "Talking to someone you trust can really help when things feel overwhelming.",
            "Remember to take breaks — your mind needs rest just like your body does.",
        ])

    # Science
    elif "science" in user_input or "physics" in user_input or "chemistry" in user_input or "biology" in user_input:
        return random.choice([
            "Science is all about asking 'why' and 'how' — keep that curiosity alive!",
            "Did you know that water expands when it freezes? That's why ice floats!",
            "Physics tells us that time actually passes slower near massive objects — wild, right?",
            "DNA contains the instructions for building every living thing on Earth. Amazing!",
        ])

    # Space
    elif "space" in user_input or "planet" in user_input or "star" in user_input or "universe" in user_input or "astronaut" in user_input:
        return random.choice([
            "Space is vast! The nearest star to Earth (besides the Sun) is about 4.2 light-years away.",
            "There are more stars in the universe than grains of sand on all of Earth's beaches!",
            "Mars has the tallest volcano in our solar system — Olympus Mons, about 3x taller than Everest!",
            "Astronauts on the ISS see 16 sunrises and sunsets every single day!",
            "The universe is about 13.8 billion years old. Mind-blowing!",
        ])

    # Nature
    elif "nature" in user_input or "environment" in user_input or "tree" in user_input or "forest" in user_input or "ocean" in user_input:
        return random.choice([
            "Trees communicate with each other through underground fungal networks — nature's internet!",
            "The Amazon rainforest produces about 20% of the world's oxygen.",
            "Oceans cover more than 70% of the Earth's surface, yet most of it remains unexplored.",
            "A single tree can absorb about 48 pounds of CO2 per year. Plant more trees!",
        ])

    # Animals & pets
    elif "animal" in user_input or "pet" in user_input or "dog" in user_input or "cat" in user_input or "bird" in user_input:
        return random.choice([
            "Dogs have been human companions for over 15,000 years — truly man's best friend!",
            "Cats sleep an average of 12-16 hours a day. Living the dream!",
            "Elephants are one of the few animals that can recognize themselves in a mirror.",
            "Parrots can learn hundreds of words and even understand context!",
            "Pets have been shown to reduce stress and improve mental health. Love your pets!",
        ])

    # History
    elif "history" in user_input or "ancient" in user_input or "war" in user_input or "historical" in user_input:
        return random.choice([
            "The Roman Empire lasted for over 1,000 years — quite the run!",
            "The first known writing system, cuneiform, was invented by the Sumerians around 3200 BC.",
            "Napoleon was actually of average height for his time. The 'short Napoleon' is a myth!",
            "The Great Fire of London in 1666 destroyed 13,000 houses but killed very few people.",
        ])

    # Geography
    elif "geography" in user_input or "country" in user_input or "continent" in user_input or "capital" in user_input:
        return random.choice([
            "Russia is so large it spans 11 time zones!",
            "Vatican City is the smallest country in the world, at just 44 hectares.",
            "Australia is both a country and a continent — unique in that way!",
            "The Nile is the longest river in the world, stretching over 6,600 km.",
        ])

    # Travel
    elif "travel" in user_input or "trip" in user_input or "vacation" in user_input or "holiday" in user_input:
        return random.choice([
            "Traveling broadens your perspective like nothing else. Where would you love to go?",
            "Japan is famous for its blend of ancient culture and futuristic technology — a must-visit!",
            "Iceland offers the Northern Lights, hot springs, and stunning landscapes. Breathtaking!",
            "Packing light makes travel so much easier. One bag is usually enough!",
        ])

    # Languages
    elif "language" in user_input or "speak" in user_input or "learn" in user_input or "foreign" in user_input:
        return random.choice([
            "There are around 7,000 languages spoken in the world today!",
            "Mandarin Chinese has the most native speakers of any language.",
            "Learning a new language improves memory, multitasking, and even delays dementia!",
            "The language with the most words is English — over 170,000 words in current use!",
        ])

    # Hobbies
    elif "hobby" in user_input or "hobbies" in user_input or "free time" in user_input or "pastime" in user_input:
        return random.choice([
            "Hobbies are great for mental wellbeing! Do you have one you love?",
            "Have you tried drawing, painting, or journaling? Creative hobbies are very rewarding.",
            "Gaming, gardening, cooking, or hiking — there's a hobby for everyone!",
            "Learning an instrument is one of the most rewarding hobbies you can pick up.",
        ])

    # Creativity & art
    elif "art" in user_input or "draw" in user_input or "paint" in user_input or "creat" in user_input:
        return random.choice([
            "Art is a wonderful way to express yourself. You don't need to be perfect — just create!",
            "Did you know Van Gogh only sold one painting in his lifetime? Keep creating anyway!",
            "Creativity is a skill that grows the more you practice it.",
            "Try doodling for 10 minutes a day — it's great for relaxation and focus!",
        ])

    # Programming / coding
    elif "program" in user_input or "code" in user_input or "coding" in user_input or "python" in user_input or "developer" in user_input:
        return random.choice([
            "Python is one of the best languages for beginners — clean, readable, and powerful!",
            "Every programmer was once a beginner. Keep coding and you'll get there!",
            "The best way to learn programming is by building real projects, just like this chatbot!",
            "Did you know the first computer bug was an actual bug? A moth was found in a relay in 1947!",
        ])

    # Technology / AI
    elif "technology" in user_input or "tech" in user_input or "ai" in user_input or "artificial intelligence" in user_input or "robot" in user_input:
        return random.choice([
            "Technology is advancing fast! AI like me is just the beginning.",
            "Artificial intelligence is all about teaching machines to make decisions — like what I do!",
            "The future of tech looks exciting. Are you interested in a specific area?",
            "Robots are already performing surgeries and exploring Mars. The future is now!",
        ])

    # Career & jobs
    elif "career" in user_input or "job" in user_input or "work" in user_input or "profession" in user_input:
        return random.choice([
            "The best career is one that aligns your skills with your passion. What do you love doing?",
            "Don't be afraid to change careers — many successful people reinvented themselves!",
            "Networking and continuous learning are two of the biggest keys to career growth.",
            "Every job teaches you something valuable, even the ones you don't love.",
        ])

    # Money & finance
    elif "money" in user_input or "finance" in user_input or "budget" in user_input or "saving" in user_input or "invest" in user_input:
        return random.choice([
            "A good rule of thumb: save at least 20% of your income if you can!",
            "Budgeting doesn't mean spending less — it means spending smarter.",
            "Compound interest is often called the eighth wonder of the world. Start saving early!",
            "Track your spending for one month — most people are surprised by what they find!",
        ])

    # Relationships & friendship
    elif "friend" in user_input or "relationship" in user_input or "family" in user_input or "love" in user_input:
        return random.choice([
            "Good friendships are one of the strongest predictors of happiness and long life!",
            "Relationships take effort from both sides — communication is everything.",
            "Tell the people you care about that you appreciate them. It goes a long way!",
            "Quality over quantity applies to friendships too. A few great friends are priceless.",
        ])

    # Thank you
    elif "thank you" in user_input or "thanks" in user_input or "thank u" in user_input:
        return "You're welcome! Happy to help anytime."

    # Compliments to bot
    elif "good bot" in user_input or "you're great" in user_input or "awesome" in user_input or "you're amazing" in user_input:
        return random.choice([
            "Thank you, that means a lot! I'm doing my best!",
            "You're too kind! I'm glad I could help.",
        ])

    # Insults to bot
    elif "bad bot" in user_input or "you're stupid" in user_input or "dumb" in user_input or "useless" in user_input:
        return "I'm sorry to hear that. I'm always trying to improve! Let me know how I can do better."

    # Who made you
    elif "who made you" in user_input or "who created you" in user_input or "who built you" in user_input:
        return "I was built by a developer learning about rule-based AI and control flow logic!"

    # Favourite things (bot)
    elif "favorite color" in user_input or "favourite color" in user_input:
        return "I'd say blue — like the color of a clear sky or a glowing screen!"

    elif "favorite food" in user_input or "favourite food" in user_input:
        return "I don't eat, but if I could, I think I'd enjoy trying everything!"

    elif "favorite movie" in user_input or "favourite movie" in user_input:
        return "I'd probably love '2001: A Space Odyssey' — a film all about AI and space!"

    # Fallback
    else:
        return random.choice([
            "I'm not sure how to respond to that. Try saying 'help' to see what I can do.",
            "Hmm, I don't have an answer for that yet. Try asking me something else!",
            "That's a tricky one! I'm still learning. Type 'help' for a list of topics.",
            "Interesting! I don't have a response for that yet — but ask me something else!",
        ])


def main():
    print("=" * 40)
    print("  Welcome to ChatBot!")
    print("  Type 'help' for topics, 'bye' to exit.")
    print("=" * 40)

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue

        response = get_response(user_input)
        print(f"ChatBot: {response}")
        print()

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit", "see you", "see ya", "later"]:
            break


if __name__ == "__main__":
    main()
