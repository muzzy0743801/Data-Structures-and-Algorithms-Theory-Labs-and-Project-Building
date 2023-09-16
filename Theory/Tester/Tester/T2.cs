using System;
using System.Collections.Generic;
using System.Text;

namespace Tester
{
    class T2
    {
        public static string BinarySearch(string[] arr, string x)
        {
            int r = arr.Length - 1;
            for (int l = 0; l <= r;)
            {
                int m = l + (r - l) / 2;

                int res = x.CompareTo(arr[m]);

                // Check if x is present at mid
                if (res == 0)
                    return Convert.ToString(m);

                // If x greater, ignore left half
                if (res > 0)
                    l = m + 1;

                // If x is smaller, ignore right half
                else
                    r = m - 1;
            }

            return "-1";
        }

        public static string BinarySearch(string[] arr, string x, int r, int l)
        {
            if (l <= r)
            {
                int m = l + (r - l) / 2;

                int res = x.CompareTo(arr[m]);

                // Check if x is present at mid
                if (res == 0)
                {
                    return Convert.ToString(m);
                }

                // If x greater, ignore left half
                if (res > 0)
                {
                    l = m + 1;
                    BinarySearch(arr, x, r, l);
                }

                // If x is smaller, ignore right half
                else
                {
                    r = m - 1;
                    BinarySearch(arr, x, r, l);
                }
            }
            return "-1";
        }
    }
}
