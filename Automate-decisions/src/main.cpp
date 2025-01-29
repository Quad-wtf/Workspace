#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <random>
#include <string>
#include <sstream>

// Function to clear the console screen
void clear_console() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

// Function to sleep for a given number of seconds
void sleep(double seconds) {
    std::this_thread::sleep_for(std::chrono::duration<double>(seconds));
}

// Function to get a random element from a vector
std::string randomize(const std::vector<std::string>& things) {
    if (things.empty()) {
        return "No items to randomize!";
    }

    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, things.size() - 1);

    return things[dis(gen)];
}

// Helper function to get ANSI color codes
std::string color(const std::string& code) {
    return "\033[" + code + "m";
}

int main() {
    clear_console();

    // Define color constants
    const std::string blue = color("34");
    const std::string yellow = color("33");
    const std::string green = color("32");
    const std::string cyan = color("36");
    const std::string red = color("31");
    const std::string reset = color("0");

    std::cout << blue << "Hello! Enter items separated by spaces to randomize, or type 'exit' to quit." << reset << std::endl;
    std::cout << yellow << "~> " << reset;

    std::string input;
    std::getline(std::cin, input);

    if (input.empty()) {
        std::cout << red << "No input provided. Exiting..." << reset << std::endl;
        return 0;
    }

    if (input == "exit" || input == "EXIT") {
        std::cout << red << "Exiting..." << reset << std::endl;
        return 0;
    }

    // Split input into items
    std::vector<std::string> things;
    std::istringstream iss(input);
    std::string item;
    while (iss >> item) {
        things.push_back(item);
    }

    if (things.empty()) {
        std::cout << red << "No valid items found to randomize!" << reset << std::endl;
        return 0;
    }

    std::cout << cyan << "Randomizing..." << reset << std::endl;
    sleep(1); // Simulate randomization delay

    std::string result = randomize(things);
    std::cout << green << "The answer is... " << yellow << result << green << "!" << reset << std::endl;

    return 0;
}

