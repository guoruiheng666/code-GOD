// #include <iostream>

// using namespace std;

// int main()
// {
//     double celsius, fahrenheit;
//     cin >> celsius;
//     fahrenheit = (celsius * 9 / 5) + 32;
//     printf("celsius=%.6f, fahrenheit=%.6f", celsius, fahrenheit);
//     return 0;
// }

// #include <iostream>

// using namespace std;

// int main()
// {
//     char low, cap;
//     cin >> low;
//     cap = low - 32;
//     cout << cap << endl;
//     return 0;
// }

// #include <iostream>
// #include <cmath>

// using namespace std;

// int main()
// {
//     int a, b;
//     double c;
//     cin >> a >> b;
//     c = sqrt(a * a + b * b);
//     printf("%.3f", c);
//     return 0;
// }

// #include <iostream>
// #include <cmath>

// using namespace std;

// int main()
// {
//     int b;
//     double x, res;
//     cin >> b >> x;
//     res = log(x) / log(b);
//     printf("%.6f", res);
//     return 0;
// }

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double a, fa, b, fb, c, fc;
    cin >> a >> fa >> b >> fb >> c;
    fc = fb + (fa - fb) * (c - b) / (a - b);
    printf("%.3f", fc);
    return 0;
}