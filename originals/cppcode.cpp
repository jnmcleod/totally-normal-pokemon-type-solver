//cppcode.cpp
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include "unistd.h"

std::string pktype;
std::map<std::string, void(*)()> fmap;
void(*fp)();

void a()
{
    std::ofstream o;
    o.open("output.txt", std::ofstream::trunc);
    o << "Type error\n";
    o.close();
    exit(0);
}


void b1()
{
    execlp("python3", "python3", "pythonfile10", NULL);
}


void b3()
{
    execlp("python3", "python3", "pythonfile1", NULL);
}


void b2()
{
    execlp("python3", "python3", "pythonfile2", NULL);
}


void b6()
{
    execlp("python3", "python3", "pythonfile3", NULL);
}


void b7()
{
    execlp("python3", "python3", "pythonfile4", NULL);
}


void b9()
{
    execlp("python3", "python3", "pythonfile7", NULL);
}


void b11()
{
    execlp("python3", "python3", "pythonfile5", NULL);
}


void b15()
{
    execlp("python3", "python3", "pythonfile6", NULL);
}


void b14()
{
    execlp("python3", "python3", "pythonfile8", NULL);
}


void b13()
{
    execlp("python3", "python3", "pythonfile9", NULL);
}


void b12()
{
    execlp("python3", "python3", "pythonfile11", NULL);
}


void b10()
{
    execlp("python3", "python3", "pythonfile12", NULL);
}


void b8()
{
    execlp("python3", "python3", "pythonfile13", NULL);
}


void b5()
{
    execlp("python3", "python3", "pythonfile14", NULL);
}


void b4()
{
    execlp("python3", "python3", "pythonfile15", NULL);
}


std::string c()
{
    fmap.insert(std::pair<std::string, void(*)()>("eci", &b1));
    fmap.insert(std::pair<std::string, void(*)()>("nogard", &b2));
    fmap.insert(std::pair<std::string, void(*)()>("retaw", &b4));
    fmap.insert(std::pair<std::string, void(*)()>("kcor", &b5));
    fmap.insert(std::pair<std::string, void(*)()>("cihcysp", &b8));
    fmap.insert(std::pair<std::string, void(*)()>("nosiop", &b10));
    fmap.insert(std::pair<std::string, void(*)()>("lamron", &b12));
    fmap.insert(std::pair<std::string, void(*)()>("dnuorg", &b13));
    fmap.insert(std::pair<std::string, void(*)()>("ssarg", &b14));
    fmap.insert(std::pair<std::string, void(*)()>("gniylf", &b15));
    fmap.insert(std::pair<std::string, void(*)()>("erif", &b11));
    fmap.insert(std::pair<std::string, void(*)()>("tsohg", &b9));
    fmap.insert(std::pair<std::string, void(*)()>("gnithgif", &b7));
    fmap.insert(std::pair<std::string, void(*)()>("cirtcele", &b6));
    fmap.insert(std::pair<std::string, void(*)()>("gub", &b3));
    return "true";
}

bool d(int selector)
{
    std::map<std::string, void(*)()>::iterator it = fmap.find(pktype);
    
    if (it == fmap.end())
    {
        a();
    }
    else
    {
        fp = it->second;
        fp();
    }
    
    return true;
}

bool e()
{
    std::ifstream file("inputs.txt");
    std::string *temp = new std::string;
    std::istringstream* parser = new std::istringstream();
    
    getline(file, *temp);
    
    parser->str(*temp);
    *parser >> pktype;
    
    file.close();
    return true;
}

int f(std::string input)
{
    switch (pktype.at(0))
    {
        case 'c':
            switch (pktype.at(1))
            {
                case 'i':
                    switch (pktype.at(2))
                    {
                        case 'h':
                            switch (pktype.at(3)) {
                                case 'c':
                                    switch (pktype.at(4)) {
                                        case 'y':
                                            switch (pktype.at(5)) {
                                                case 's':
                                                    switch (pktype.at(6)) {
                                                        case 'p':
                                                            d(13);
                                                            break;
                                                            
                                                        default:
                                                            a();
                                                            break;
                                                    }
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                         
                        case 'r':
                            switch (pktype.at(3)) {
                                case 't':
                                    switch (pktype.at(4)) {
                                        case 'c':
                                            switch (pktype.at(5)) {
                                                case 'e':
                                                    switch (pktype.at(6)) {
                                                        case 'l':
                                                            switch (pktype.at(7)) {
                                                                case 'e':
                                                                    d(3);
                                                                    break;
                                                                    
                                                                default:
                                                                    a();
                                                                    break;
                                                            }
                                                            break;
                                                            
                                                        default:
                                                            a();
                                                            break;
                                                    }
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                default:
                    a();
                    break;
            }
            break;
            
            
        case 'd':
            switch (pktype.at(1))
            {
                case 'n':
                    switch (pktype.at(2))
                    {
                        case 'u':
                            switch (pktype.at(3))
                            {
                                case 'o':
                                    switch (pktype.at(4))
                                    {
                                        case 'r':
                                            switch (pktype.at(5))
                                            {
                                                case 'g':
                                                    d(9);
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                
                                default:
                                    a();
                                    break;
                            }
                            
                        default:
                            a();
                            break;
                    }
                    
                default:
                    a();
                    break;
            }
            break;
            
          
        case 'e':
            switch (pktype.at(1))
            {
                case 'c':
                    switch (pktype.at(2))
                    {
                        case 'i':
                            d(10);
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                case 'r':
                    switch (pktype.at(2))
                    {
                        case 'i':
                            switch (pktype.at(3))
                            {
                                case 'f':
                                    d(5);
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                default:
                    a();
                    break;
            }
        
        
        case 'g':
            switch (pktype.at(1)) {
                case 'n':
                    switch (pktype.at(2)) {
                        case 'i':
                            switch (pktype.at(3))
                            {
                                case 't':
                                    switch (pktype.at(4))
                                    {
                                        case 'h':
                                            switch (pktype.at(5)) {
                                                case 'g':
                                                    switch (pktype.at(6)) {
                                                        case 'i':
                                                            switch (pktype.at(7)) {
                                                                case 'f':
                                                                    d(4);
                                                                    break;
                                                                    
                                                                default:
                                                                    a();
                                                                    break;
                                                            }
                                                            break;
                                                            
                                                        default:
                                                            a();
                                                            break;
                                                    }
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                case 'y':
                                    switch (pktype.at(4)) {
                                        case 'l':
                                            switch (pktype.at(5)) {
                                                case 'f':
                                                    d(6);
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                case 'u':
                    switch (pktype.at(2)) {
                        case 'b':
                            d(1);
                            break;
                            
                        default:
                            a();
                            break;
                    }
                default:
                    a();
                    break;
            }
            break;
            
        
        case 'k':
            switch (pktype.at(1)) {
                case 'c':
                    switch (pktype.at(2)) {
                        case 'o':
                            switch (pktype.at(3)) {
                                case 'r':
                                    d(14);
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                default:
                    a();
                    break;
            }
            break;
            
        
        case 'l':
            switch (pktype.at(1)) {
                case 'a':
                    switch (pktype.at(2)) {
                        case 'm':
                            switch (pktype.at(3)) {
                                case 'r':
                                    switch (pktype.at(4)) {
                                        case 'o':
                                            switch (pktype.at(5)) {
                                                case 'n':
                                                    d(11);
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                default:
                    a();
                    break;
            }
            break;
            
        case 'n':
            switch (pktype.at(1)) {
                case 'o':
                    switch (pktype.at(2)) {
                        case 'g':
                            switch (pktype.at(3)) {
                                case 'a':
                                    switch (pktype.at(4)) {
                                        case 'r':
                                            switch (pktype.at(5)) {
                                                case 'd':
                                                    d(2);
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        case 's':
                            switch (pktype.at(3)) {
                                case 'i':
                                    switch (pktype.at(4)) {
                                        case 'o':
                                            switch (pktype.at(5)) {
                                                case 'p':
                                                    d(12);
                                                    break;
                                                    
                                                default:
                                                    a();
                                                    break;
                                            }
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                default:
                    a();
                    break;
            }
            break;
        
        case 'r':
            switch (pktype.at(1)) {
                case 'e':
                    switch (pktype.at(2)) {
                        case 't':
                            switch (pktype.at(3)) {
                                case 'a':
                                    switch (pktype.at(4)) {
                                        case 'w':
                                            d(15);
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                default:
                    a();
                    break;
            }
            break;
           
        case 's':
            switch (pktype.at(1)) {
                case 's':
                    switch (pktype.at(2)) {
                        case 'a':
                            switch (pktype.at(3)) {
                                case 'r':
                                    switch (pktype.at(4)) {
                                        case 'g':
                                            d(8);
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                default:
                    a();
                    break;
            }
            break;
            
        case 't':
            switch (pktype.at(1)) {
                case 's':
                    switch (pktype.at(2)) {
                        case 'o':
                            switch (pktype.at(3)) {
                                case 'h':
                                    switch (pktype.at(4)) {
                                        case 'g':
                                            d(7);
                                            break;
                                            
                                        default:
                                            a();
                                            break;
                                    }
                                    break;
                                    
                                default:
                                    a();
                                    break;
                            }
                            break;
                            
                        default:
                            a();
                            break;
                    }
                    break;
                    
                default:
                    a();
                    break;
            }
            break;
            
        default:
            a();
            break;
    }
    return -1;
}

int main(int argc, const char * argv[])
{
    c();
    
    if (e())
    {
        f("attacking type");
    }
    
    
    return 0;
}
