#include<iostream>
#include<math.h>
using namespace std;

void gen(int b[], bool &stop, int n)
{
    int i = n - 1;
    while(i >= 0 && b[i] == 1)
    {
        b[i] = 0;
        --i;
    }
    if(i == -1) stop = true;
    else b[i] = 1;

}

int main()
{
	int n, k;
	cin >> n >> k;
	int *A = new int[n];
    int b[n];
	for(int i = 0; i < n; i++)
    {
        cin >> A[i];
        b[i] = 0;
    }
    bool stop = false;
    int count = 0;
	while(!stop)
    {
        gen(b, stop, n);
        int sum = 0;
        for(int i = 0; i < n; i++)
        {
            if(b[i] == 1) sum += A[i];
        }
        if(sum == k)
        {
            for(int i = 0; i < n; i++)
            {
                if(b[i] == 1) cout << A[i] << " ";
            }
            cout << endl;
            ++count;
        }
    }
    cout << count << endl;
}