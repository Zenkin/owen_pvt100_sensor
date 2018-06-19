#include <stdio.h>
#include <string.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close
#include <termios.h> 

#include <linux/serial.h>

// Include definition for RS485 ioctls: TIOCGRS485 and TIOCSRS485
#include <sys/ioctl.h>

int fd;
int rts_delay_before_send = 0, rts_delay_after_send = 0;

int main() {

	printf ("starting RS485_serial_communications");

	/* Open your specific device (e.g., /dev/mydevice): */
	fd = open ("/dev/ttyUSB0", O_RDWR);
	if (fd < 0) {
		perror("Unable to open port");
	}

	printf ("the device was opened successfully");

	struct serial_rs485 rs485conf;

	// Enable RS485 mode
	rs485conf.flags |= SER_RS485_ENABLED;

	// Set logical level for RTS pin equal to 1 when sending
	rs485conf.flags |= SER_RS485_RTS_ON_SEND;
	// or, set logical level for RTS pin equal to 0 when sending
	rs485conf.flags &= ~(SER_RS485_RTS_ON_SEND);
	
	//Set logical level for RTS pin equal to 1 after sending
	rs485conf.flags |= SER_RS485_RTS_AFTER_SEND;
	// or, set logical level for RTS pin equal to 0 after sending
	rs485conf.flags &= ~(SER_RS485_RTS_AFTER_SEND);

	// Set rts delay before send
	rs485conf.delay_rts_before_send = rts_delay_before_send;

	// Set rts delay after send
	rs485conf.delay_rts_after_send = rts_delay_after_send;

	//bSet this flag if you want to receive data even whilst sending data
	rs485conf.flags |= SER_RS485_RX_DURING_TX;

	if (ioctl (fd, TIOCSRS485, &rs485conf) < 0) {
	}

	// Use read() and write() syscalls here...

	// Close the device when finished
	if (close (fd) < 0) {
		perror("Unable to close port");
	}

	printf ("the device was closed successfully");

	return 0;
}