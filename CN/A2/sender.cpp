#include<iostream>
#include<vector>
#include<stdlib.h>
using namespace std;

class Sender
{
	vector<int> dataword;
	vector<int> codeword;
	vector<int> generator;
	vector<int> receivedCw;
	int k;
	int r;
	int n;	
	int g;
	public:
	Sender()
	{
		generator.push_back(1);
		generator.push_back(0);
		generator.push_back(1);
		generator.push_back(1);
		k = r = n = 0;
		g = 4;
	}
	void acceptData()
	{
		label:
		cout<<"Enter the dataword"<<endl;
		string dw;
		cin>>dw;
		if(dw[0]=='0')
		{
			cout<<"***** Dataword cannot start with 0******\n";
			goto label;
		}
		for(int i = 0; i< dw.size(); i++)
		{
			dataword.push_back(dw[i] - 48);
		}
		k = dw.size();	
	}
	void calculate_append()
	{
		n = g + k - 1;
		r = n - k;

	}
	void calc_code()
	{
		int i,j,l;
		for(i=0;i<k;i++)
		{
			codeword.push_back(dataword[i]);
		}
		for(i=0;i<r;i++)
		{
			codeword.push_back(0);
		}
		cout<<"\nafter appending zeroes:";
		for(i=0;i<codeword.size();i++)
		{
			cout<<codeword[i];
		}
		//cout<<endl;
		for(i=0;i<k;i++)
	    {
	        j=0;
	        l=i;
	        //check whether it is divisible or not
	        if (codeword[l]>=generator[j])
	        {
	            for(j=0,l=i;j<g;j++,l++)
	            {
	                if((codeword[l]==1 && generator[j]==1) || (codeword[l]==0 && generator[j]==0))
	                {
	                    codeword[l]=0;
	                }
	                else
	                {
	                    codeword[l]=1;
	                }
	            }
	        }
	    }
			vector<int> crc(n);
			for(i=0,j=k;i<r;i++,j++)
	    {
	        crc[i]=codeword[j];
	    }

			//cout<<endl;
	    cout<<"\nso code word generated for transmission:\n";
			codeword.clear();
			for(i=0;i<k;i++)
			{
				codeword.push_back(dataword[i]);
			}
			for(i=0;i<r;i++)
			{
				codeword.push_back(crc[i]);
			}
			for(i=0;i<n;i++)
			{
				cout<<codeword[i];
			}
			//cout<<endl;
	}

	void transmit()
	{
		char ch;
		int c;
		cout<<"\ndo you want to transmit the generated codeword,y for yes:";
		cin>>ch;
		if(ch=='y'||ch=='Y')
		{
			for(int i=0;i<n;i++)
			{
				receivedCw.push_back(codeword[i]);
			}
		}
		else
		{
			for(int i=0;i<n;i++)
			{
				receivedCw.push_back(codeword[i]);
			}
			cout<<"\nwhich bit you want to change:";
			cin>>c;
			if(codeword[c]==0)
			{
				receivedCw[c]=1;
			}
			else
				receivedCw[c]=0;
		}
		cout<<"\nthe codeword transmitted will be:\n";
				for(int i=0;i<n;i++)
				{
					cout<<receivedCw[i];
				}
				cout<<endl;
	}

	void check()
	{
		int i,j,l;
		    for(i=0;i<k;i++)
	    {
	        j=0;
	        l=i;
	        if (receivedCw[l]>=generator[j])
	        {
	            for(j=0,l=i;j<g;j++,l++)
	            {
	                if((receivedCw[l]==1 && generator[j]==1) || (receivedCw[l]==0 && generator[j]==0))
	                {
	                    receivedCw[l]=0;
	                }
	                else
	                {
	                    receivedCw[l]=1;
	                }
	            }
	        }
	    }
			cout<<"\nRemainder: ";
			vector<int> rem(r);
			for (i=k,j=0;i<n;i++,j++)
			{
					rem[j]= receivedCw[i];
			}
			for(i=0;i<r;i++)
			{
					cout<<rem[i];
			}

			int flag=0;
			for(i=0;i<r;i++)
			{
					if(rem[i]!=0)
					{
							flag=1;
					}
			}

			if(flag==0)
			{
					cout<<"\nAs Syndrome is 0,CRC pass\n";

			}
			else
			{
					cout<<"\nSince Syndrome is not 0,CRC fail\n";
			}
	}
};

int main()
{
	Sender e;
	e.acceptData();
	e.calculate_append();
	e.calc_code();
	e.transmit();
	e.check();
	return 0;
}
