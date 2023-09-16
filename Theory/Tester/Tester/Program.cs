using System;
using System.Linq;

namespace Tester
{
    class Program
    {
        public static int factorial(int i)
        {
            if (i < 1)
                return 1;
            return i * factorial(i - 1);
        }
        static void Main()
        {
            A(5);
            int[,] arr2d = new int[3, 3]{ {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
            for (int i = 0; i <= arr2d.GetLength(0) - 1; i++)
            {
                if ((arr2d.GetLength(0) - 1) / 2 != i)
                {
                    int temp = arr2d[i, 0];
                    arr2d[i, 0] = arr2d[i, 2];
                    arr2d[i, 2] = temp;
                }
            }
            foreach (int x in arr2d)
            {
                Console.WriteLine(x);
            }
        }

        public static void A(int n)
        {
            if (n > 1)
            {
                A(n - 1);
            }
            Console.WriteLine(n);
            return;
        }
        public static void Adder(string[] array, string[] temp, string name)
        {
            int mid = (0 + array.Length) / 2;
            array = new string[temp.Length + 1];
            for (int i = 0; i < array.Length; i++)
            {
                if (i <= mid)
                {
                    array[i] = temp[i];
                }
                else if (i == mid + 1)
                {
                    array[i] = name;
                }
                else
                {
                    array[i] = temp[i-1];
                }
            }
            PrintArray(array);
        }

        public static void PrintArray(string[] array)
        {
            int n = array.Length;
            for (int i = 0; i < n; ++i)
                Console.Write(array[i] + " ");
            Console.WriteLine();
        }
    }
}
