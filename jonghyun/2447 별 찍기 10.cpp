#include <iostream>
#include <vector>
#include <string>

void star2(int n)
{
	for (int i = n; i > 0; i--)
	{
		int count = 0;
		for (int j = i - 1; j > 0; j--)
		{
			std::cout << " ";
			count++;
		}
		while (count < n)
		{
			std::cout << "*";
			count++;
		}
		std::cout << "\n";
	}
}

void star3(int n)
{
	for (int i = n; i > 0; i--)
	{
		for (int j = 0; j < i; j++)
		{
			std::cout << "*";
		}
		std::cout << "\n";
	}
}

void star4(int n)
{
	for (int i = 0; i < n; i++)
	{
		int count = 0;
		for (int j = i - 1; j >= 0; j--)
		{
			std::cout << " ";
			count++;
		}
		while (count < n)
		{
			std::cout << "*";
			count++;
		}
		std::cout << "\n";
	}
}

void star5(int n)
{
	for (int i = 0; i < n; i++)
	{
		int j = n - 1;
		for (; j > i; j--)
		{
			std::cout << " ";
		}
		int j_ = j;
		for (; j > 0; j--)
		{
			std::cout << "*";
		}
		std::cout << "*";
		for (; j_ > 0; j_--)
		{
			std::cout << "*";
		}
		std::cout << "\n";
	}
}

void star6(int n)
{
	for (int i = n - 1; i >= 0; i--)
	{
		int j = n - 1;
		for (; j > i; j--)
		{
			std::cout << " ";
		}
		int j_ = j;
		for (; j > 0; j--)
		{
			std::cout << "*";
		}
		std::cout << "*";
		for (; j_ > 0; j_--)
		{
			std::cout << "*";
		}
		std::cout << "\n";
	}
}

void star7(int n)
{
	star5(n);
	n--;
	std::cout << " ";
	for (int i = n - 1; i >= 0; i--)
	{
		int j = n - 1;
		for (; j > i; j--)
		{
			std::cout << " ";
		}
		int j_ = j;
		for (; j > 0; j--)
		{
			std::cout << "*";
		}
		std::cout << "*";
		for (; j_ > 0; j_--)
		{
			std::cout << "*";
		}
		std::cout << "\n ";
	}
}

void star8(int n)
{
	for (int i = 0; i < n; i++)
	{
		int j = 0;
		for (; j <= i; j++)
		{
			std::cout << "*";
		}
		for (; j < n; j++)
		{
			std::cout << "  ";
		}
		j = 0;
		for (; j <= i; j++)
		{
			std::cout << "*";
		}

		std::cout << "\n";
	}
	n--;
	for (int i = n - 1; i >= 0; i--) 
	{
		int j = 0;
		for (; j <= i; j++)
		{
			std::cout << "*";
		}
		for (; j <= n; j++)
		{
			std::cout << "  ";
		}
		j = 0;
		for (; j <= i; j++)
		{
			std::cout << "*";
		}

		std::cout << "\n";
	}

}

void star9(int n)
{
	star6(n);
	for (int i = 1; i < n; i++)
	{
		int j = n - 1;
		for (; j > i; j--)
		{
			std::cout << " ";
		}
		int j_ = j;
		for (; j > 0; j--)
		{
			std::cout << "*";
		}
		std::cout << "*";
		for (; j_ > 0; j_--)
		{
			std::cout << "*";
		}
		std::cout << "\n";
	}
}

void star10core(std::vector<std::string> &field,int n,int offsetX,int offsetY) 
{
	if (n < 3)
		return;
	n /= 3;
	for (int i = offsetY+n; i < offsetY + 2*n; i++)
		for (int j = offsetX+n; j < offsetX + 2*n; j++)
			field[i][j] = ' ';
	for(int i=0;i<3;i++)
		for (int j = 0; j < 3; j++)
		{
			star10core(field, n, offsetX + j * n, offsetY + i * n);
		}
}
void star10(int n)
{
	std::string standard(n,'*');
	std::vector<std::string> field(n,standard);

	star10core(field, n, 0, 0);
	
	for (int i = 0; i < n; i++)
		std::cout << field[i] << "\n";
}

int main()
{
	int n;
	std::cin >> n;

	star10(n);

	return 0;
}
