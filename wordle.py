import random

word_list = [
    "apple", "apply", "argue", "arise", "armed", "array", "aside", "asset", "audio", "audit",
    "avoid", "awake", "aware", "awful", "badge", "baker", "basic", "basis", "beach", "began",
    "begin", "begun", "being", "below", "bench", "billy", "birth", "black", "blame", "blank",
    "blind", "block", "blood", "board", "boost", "booth", "bound", "brain", "brand", "bread",
    "break", "breed", "brief", "bring", "broad", "broke", "brown", "brush", "buddy", "build",
    "built", "burst", "carry", "catch", "cause", "chain", "chair", "chart", "chase", "cheap",
    "check", "chest", "chief", "child", "china", "choke", "civil", "claim", "class", "clean",
    "clear", "click", "clock", "close", "coach", "coast", "could", "count", "court", "cover",
    "craft", "crash", "cream", "crime", "cross", "crowd", "crown", "curve", "cycle", "daily",
    "dance", "dated", "dealt", "death", "debut", "delay", "depth", "diary", "digit", "dirty",
    "disco", "ditch", "doing", "donor", "doubt", "draft", "drama", "drawl", "drawn", "dream",
    "dress", "drill", "drink", "drive", "dwell", "early", "earth", "eight", "elbow", "elite",
    "empty", "enemy", "enjoy", "enter", "entry", "equal", "error", "event", "every", "exact",
    "exist", "extra", "faint", "faith", "false", "fault", "favor", "feast", "fetch", "fever",
    "field", "fifth", "fifty", "fight", "final", "first", "fixed", "flame", "flash", "fleet",
    "floor", "flour", "fluid", "focus", "force", "forum", "found", "frame", "fraud", "fresh",
    "front", "fruit", "funny", "giant", "given", "glass", "glove", "going", "grant", "grave",
    "great", "green", "greet", "gross", "group", "grown", "guard", "guess", "guest", "guide",
    "habit", "happy", "harsh", "haven", "heart", "heavy", "hence", "hinge", "house", "human",
    "humor", "ideal", "image", "index", "inner", "input", "issue", "joint", "judge", "known",
    "label", "large", "later", "laugh", "layer", "learn", "least", "leave", "legal", "lemon",
    "level", "light", "limit", "local", "logic", "loose", "lower", "lucky", "lunch", "major",
    "maker", "march", "marry", "match", "maybe", "mayor", "meant", "medal", "media", "metal",
    "might", "minor", "minus", "mixed", "model", "money", "month", "moral", "motor", "mount",
    "mouse", "mouth", "movie", "music", "needs", "never", "night", "noted", "novel", "nurse",
    "occur", "ocean", "offer", "often", "order", "other", "outer", "owner", "panel", "panic",
    "party", "peace", "phase", "phone", "photo", "piece", "pilot", "pitch", "place", "plain",
    "plane", "plant", "plate", "point", "pound", "power", "press", "price", "pride", "prime",
    "print", "prior", "prize", "proof", "proud", "prove", "queen", "quick", "quiet", "quite",
    "radio", "raise", "range", "rapid", "ratio", "reach", "react", "ready", "realm", "rear",
    "reason", "rebel", "refer", "relax", "reply", "reset", "right", "rigid", "rival", "river",
    "robot", "rocky", "roman", "royal", "rugby", "ruler", "rural", "salon", "sauce", "scale",
    "scene", "scope", "score", "scout", "sense", "serve", "seven", "shade", "shaft", "shake",
    "shall", "shame", "shape", "share", "sharp", "sheet", "shelf", "shell", "shift", "shine",
    "shirt", "shock", "shoot", "shore", "short", "shout", "shown", "sight", "since", "skill",
    "skirt", "sleep", "slice", "slide", "slope", "small", "smart", "smell", "smile", "smoke",
    "solid", "solve", "sorry", "sound", "south", "space", "spare", "speak", "speed", "spend",
    "spent", "split", "spoil", "sport", "staff", "stage", "stain", "stake", "stand", "start",
    "state", "steam", "steel", "steep", "stick", "still", "stock", "stone", "stood", "store",
    "storm", "story", "strip", "stuff", "style", "sugar", "suite", "super", "sweet", "table",
    "taken", "taste", "teach", "teeth", "texas", "thank", "theft", "their", "theme", "there",
    "these", "thick", "thing", "think", "third", "those", "three", "throw", "tight", "title",
    "today", "topic", "total", "touch", "tough", "tower", "track", "trade", "train", "treat",
    "trend", "trial", "tribe", "trick", "tried", "truck", "truly", "trust", "truth", "twice",
    "twist", "under", "union", "unity", "until", "upper", "urban", "usage", "usual", "value",
    "video", "visit", "vital", "voice", "voter", "waste", "watch", "water", "wheel", "where",
    "which", "while", "white", "whole", "whose", "woman", "women", "world", "worry", "worth",
    "would", "wound", "write", "wrong", "wrote", "yield", "young", "youth"
]

secret_word = random.choice(word_list)

print("You have 5 chances to guess the 5-letter word. Good luck!\n")
print("--------------------------------")

# Function for checking if guessed word is 5-lettered or not
def guess_checker(guessed):
    if len(guessed) != 5:
        print("Not enough letters, Please try again")
        print("----*----*----*----*----*")
    else:
        print(guessed)

# Main line of code
guesses = 0
while guesses < 5:
    correct_letters = 0
    guessed_word = input("Please enter your guess: ").lower()  # Convert input to lowercase
   
    guess_checker(guessed_word)
   
    if guessed_word == secret_word and len(guessed_word) == 5:
        guesses += 1
        print("Valid guess number", guesses)
        print("Correct!")
        break
    elif len(guessed_word) == 5 and secret_word != guessed_word:
        print("Incorrect, try again")
        for i in range(min(len(secret_word), len(guessed_word))):
            if secret_word[i] == guessed_word[i]:
                # If the letters at the current position match, increment the correct_letters
                print("Correct letter @ position", i+1)
                correct_letters += 1
       
        print(correct_letters, "letter(s) is/are in the correct position.\n")
       
        guesses += 1  # Move this line inside the loop but after the condition
        print("Valid guess number", guesses)
        print("--------------------------------")

print("GAME OVER")
print("Correct word was:", secret_word)
