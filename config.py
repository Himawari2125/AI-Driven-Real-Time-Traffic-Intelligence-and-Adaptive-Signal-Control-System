import os

# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SUMO_DIR = os.path.join(
    BASE_DIR,
    "sumo"
)

SUMO_CONFIG = os.path.join(
    SUMO_DIR,
    "RL.sumocfg"
)

# SUMO executable
SUMO_HOME = os.environ.get(
    "SUMO_HOME",
    r"E:\Thapar\Data Science\sumo-win64-1.28.0"
)

SUMO_BINARY = os.path.join(
    SUMO_HOME,
    "bin",
    "sumo.exe"
)

SUMO_GUI_BINARY = os.path.join(
    SUMO_HOME,
    "bin",
    "sumo-gui.exe"
)


# ============================================================
# REINFORCEMENT LEARNING SETTINGS
# ============================================================

LEARNING_RATE = 0.1

DISCOUNT_FACTOR = 0.95

EPSILON = 1.0

EPSILON_MIN = 0.01

EPSILON_DECAY = 0.995


# ============================================================
# TRAFFIC SIGNAL SETTINGS
# ============================================================

MIN_GREEN_TIME = 10

MAX_GREEN_TIME = 60

YELLOW_TIME = 3

ACTION_SPACE = [
    0,  # Keep current phase
    1,  # Change phase
]


# ============================================================
# SIMULATION SETTINGS
# ============================================================

SIMULATION_STEP = 0

TOTAL_STEPS = 5000

GUI_MODE = True


# ============================================================
# OUTPUT / DATA SETTINGS
# ============================================================

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

RESULTS_DIR = os.path.join(
    BASE_DIR,
    "results"
)

DATASET_FILE = os.path.join(
    DATA_DIR,
    "traffic_data.csv"
)

RESULTS_FILE = os.path.join(
    RESULTS_DIR,
    "rl_results.csv"
)


# ============================================================
# CREATE REQUIRED DIRECTORIES
# ============================================================

os.makedirs(
    DATA_DIR,
    exist_ok=True
)

os.makedirs(
    RESULTS_DIR,
    exist_ok=True
)


# ============================================================
# CHECK CONFIGURATION
# ============================================================

def check_configuration():

    problems = []

    if not os.path.exists(SUMO_DIR):
        problems.append(
            f"SUMO project folder not found: {SUMO_DIR}"
        )

    if not os.path.exists(SUMO_CONFIG):
        problems.append(
            f"SUMO configuration not found: {SUMO_CONFIG}"
        )

    if not os.path.exists(SUMO_BINARY):
        problems.append(
            f"SUMO executable not found: {SUMO_BINARY}"
        )

    return problems


# ============================================================
# PRINT CONFIGURATION
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("SUMO-RL PROJECT CONFIGURATION")
    print("=" * 60)

    print(f"Project directory : {BASE_DIR}")
    print(f"SUMO directory    : {SUMO_DIR}")
    print(f"SUMO config       : {SUMO_CONFIG}")
    print(f"SUMO executable   : {SUMO_BINARY}")

    print("-" * 60)

    problems = check_configuration()

    if problems:

        print("Configuration problems:")

        for problem in problems:
            print(f"  ❌ {problem}")

    else:

        print("✅ Configuration is valid.")

    print("=" * 60)