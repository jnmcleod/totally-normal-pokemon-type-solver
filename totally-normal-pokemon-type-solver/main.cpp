#include <fstream>
#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

extern char** environ;

void createFiles()
{
    std::ifstream inputFile("sourcecode");
    if (!inputFile)
    {
        std::cout << "Source file not found\n";
        exit(-1);
    }
    
    std::ofstream outputFile;
    std::string temp;
    
    while (getline(inputFile, temp))
    {
        if (temp[0] == '/' && temp[1] == '/')
        {
            outputFile.close();
            outputFile.open(&temp[2], std::ofstream::app);
        }
        else
        {
            outputFile << temp << std::endl;
        }
    }
    
    inputFile.close();
    outputFile.close();
}

void compileFiles()
{
    pid_t child = fork();
    if (child == 0)
    {
        int fd = open("log.txt", O_WRONLY | O_TRUNC | O_CREAT, S_IRUSR | S_IWUSR);
        dup2(fd, STDERR_FILENO);
        execlp("javac", "javac", "Javacode.java", NULL);
    }
    else
    {
        child = fork();
        if (child == 0)
        {
            execlp("g++", "g++", "-o", "cppcode", "cppcode.cpp", NULL);
        }
    }
    
}

int main()
{
    createFiles();
    compileFiles();
    
    return 0;
}
