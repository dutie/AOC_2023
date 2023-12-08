#include <cctype>
#include <cstddef>
#include <iostream>
#include <ostream>
#include <string>

std::string
parse_line (const std::string &line)
{
  std::string strDigits = "";
  for (char ch : line)
    {
      if (isdigit (ch))
        {
          strDigits.push_back (ch);
        }
    }
  std::string fValue = std::string (1, strDigits.front ());
  if (strDigits.length () > 1)
    {
      fValue + std::string (1, strDigits.back ());
    }
  return fValue;
}

int
main ()
{
  std::string example = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet";
  std::size_t startPos = 0;
  std::size_t endPos = example.find ('\n', startPos);
  int result = 0;
  while (startPos != std::string::npos)
    {
      std::string line = example.substr (startPos, endPos - startPos);
      std::string parsedLine = parse_line (line);
      int calibrationValue = std::stoi (parsedLine);
      result += calibrationValue;
      std::cout << "Original Line: " << line
                << ", Calibration Value: " << calibrationValue << std::endl;
      startPos = endPos + 1;
      endPos = example.find ('\n', startPos);
    }
  return 0;
}
