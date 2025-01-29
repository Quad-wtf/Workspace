#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <stdlib.h>

void showBalance(double balance);
double deposit();
double withdraw(double balance);

int main() {

    system("color 4");

    double balance = 0;
    int choice = 0;

    do {
        
    std::cout << "********************\n";
    std::cout << "POLSKI BANK NARODOWY\n";
    std::cout << "********************\n";
    std::cout << "Wybierz obcje: \n";
    std::cout << "1. Pokaz balans\n";
    std::cout << "2. Wykonaj wplate\n";
    std::cout << "3. Wykonaj wyplate\n";
    std::cout << "4. Wyjdz\n";
    std::cin >> choice;

    switch(choice) {
        case 1: // Pokaż balans
                showBalance(balance);
                break;
        case 2: // Wykonaj wpłatę
                balance += deposit();
                showBalance(balance);
                break;
        case 3: // Wykonaj wypłatę
                balance -= withdraw(balance);
                showBalance(balance);
                break;
        case 4: // Wyjdź
                std::cout << "Dziekujemy za wizyte!\n";
                _sleep(2000);
                break;
        default: // Zła odpowiedź
                std::cout << "Zla odpowiedź";
    }

    }while(choice != 4);

    return 0;
}

void showBalance(double balance)
{
    std::cout << "Twoj biezacy balans to: " << std::setprecision(2) << std::fixed << balance << "PLN.\n";
    if (balance == 0)
    {
        std::cout << "Slabiutko :(\n\n\n";
    }
    if (balance == 1){
        std::cout << "Przynajmiej nie jest to 0... hehe...\n\n\n";
    }
    if (balance == 1000){
        std::cout << "Ladnie ladnie... :)\n\n\n";
    }
    if (balance == 10000){
        std::cout << "Wow! W jakiej pracy pracujesz? szybko zarabiasz! :O\n\n\n";
    }
    if (balance == 100000){
        std::cout << "Brawo! Brawo! Sto tysiecy zlotych... :)\n\n\n";
    }
    if (balance > 1000000){
        std::cout << "Dzień dobry szanowny panie :D\n\n\n";
    }
}
double deposit(){

    double amount = 0;

    std::cout << "Podaj kwote wplaty: ";
    std::cin >> amount;

    if (amount > 0){
        return amount;
    }
    else{
        std::cout << "Chcesz być zadłużony? Nie pozwolę ci mieć negatywnych pieniędzy!\n";
        return 0;
        std::cout << "\n\n\n";
    }

    system("cls");
    std::cout << "Wplata przebiegla pomyslnie. \n\n\n";
}

double withdraw(double balance) {
    return 0;
}
