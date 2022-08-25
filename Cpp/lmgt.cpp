#include <iostream>
#include <string>
#include <vector>

#include "cpparser.cpp"


namespace clipboard {
	void copy(std::string text_to_copy) {
		std::string scommand = "echo " + text_to_copy + " | xclip -selection c";
		char command[scommand.size()];

		for (int i = 0; i < scommand.size(); i++) command[i] = scommand[i];

		system(command);
	}
}


std::string join(std::vector<std::string> to_join, std::string joiner) {
	std::string result = "";

	for (int i = 0; i < to_join.size(); i++) {
		result += to_join[i];

		if (i != to_join.size()-1) {
			result += joiner;
		}
	}

	return result;
}


int main(int argc, char** argv) {
	#ifdef __linux__
	const std::string LMGT_URL="https://letmegooglethat.com/?q=";
	Parser parser("A little CLI to copy queries from letmegooglethat");

	parser.addArgument(
		"-q",
		"--query",
		"query",
		true,
		Parser::STORE_MULTIPLE_VALUES,
		"The user query"
	);

	auto args = parser.parseArgs(argc, argv);

	if (args["query"].Vector.size() == 0) return 0;

	std::string query_url = LMGT_URL + join(args["query"].Vector, "+");

	clipboard::copy(query_url);

	#else
		std::cout << "Your actual OS is not supported by this program, which means you do not use GNU/Linux based operating system.\nWe will find you and convert you.\n\nHail Linus" << std::endl;
		return 0;
	#endif

	return 0;
}
