/*#include<iomanip>
using namespace std;


int main()
{
	int choice;
	string sr_no,time,source,destination,protocol,len,info;

	do
	{
		ifstream file("asach.csv");
		int count = -1;
		int i = 0;

		cout<<"Enter choice 1 2 3 4 5 6 "<<endl;
		cin>>choice;

		string protocolchoice;

		switch(choice)
		{
			case 1: protocolchoice = "IP/TCP/UDP";
			break;

			default : cout<<"\nWrong choice";
			   break;
		}

		while(file.good() and choice != 0)
		{
			getline(file,sr_no,',');
			getline(file,time,',');
			getline(file,source,',');
			getline(file,destination,',');
			getline(file,protocol,',');
			getline(file,len,',');
			getline(file,info,'\n');

			protocol = string(protocol,1,protocol.length()-2);

            if(protocol == "Protocol" || choice == protocolchoice || protocolchoice == All)
            {
            	cout <<setw(4)<<left<<i++;
				cout << setw(30)<<left<<string( source, 1, source.length()-2 );
				cout << setw(30)<<left<<string( destination, 1, destination.length()-2 );
				cout <<setw(8)<<left<<protocol;
				cout <<setw(8)<<left<< string( len, 1, len.length()-2 );
				cout << string( info, 1, info.length()-2 )<<"\n\n";
				count++;
            }

		}

		file.close();
        if(choice != 0)
        {
        	cout<<"Count is: "<<count;
        } 


	}while(choice != 0);

	return 0;
}
*/




#include <iostream>
#include<fstream>
#include <iomanip>
#include<string>
using namespace std;

int main() {
	cout << "***** PACKET ANALYZER *****" << endl; 
	string value, sr_no,time,source,destination,info,protocol,len;
	int count=-1,i=0;



	int choice;
	do
	{
		ifstream file("asach.csv");
		count=-1;
		i=0;
		cout<<"\nEnter which protocol packets you want to see"<<endl;
		cout<<"1.IP\n2.UDP\n3.TCP\n4.Ethernet\n5.ALL\n0Exit\nChoice:"<<endl;
		cin>>choice;
		string protocolChoice;
		switch(choice){
		case 1: protocolChoice="ICMP";
		break;
		case 2: protocolChoice="UDP";
		break;
		case 3: protocolChoice="TCP";
		break;
		case 4: protocolChoice="ARP";
		break;
		case 5: protocolChoice="ALLPROTOCOLS";
		break;
		default: protocolChoice="ARP";
		break;
		}
		while(file.good() and choice!=0)
		{
			getline(file,sr_no,',');
			getline(file,time,',');
			getline(file,source,',');
			getline(file,destination,',');
			getline(file,protocol,',');
			getline(file,len,',');
			getline(file,info,'\n');

			protocol=string(protocol,1,protocol.length()-2);

			if(protocol=="Protocol"||protocol==protocolChoice||protocolChoice=="ALLPROTOCOLS")
			{
				cout <<setw(4)<<left<<i++;
				cout << setw(30)<<left<<string( source, 1, source.length()-2 );
				cout << setw(30)<<left<<string( destination, 1, destination.length()-2 );
				cout <<setw(8)<<left<<protocol;
				cout <<setw(8)<<left<< string( len, 1, len.length()-2 );
				cout << string( info, 1, info.length()-2 )<<"\n\n";
				count++;
			}
		}
		file.close();
		if(choice!=0)
		cout<<"\nTotal Packet Count: "<<count<<endl;
	}while(choice!=0);
	return 0;
}
















































































































































































































