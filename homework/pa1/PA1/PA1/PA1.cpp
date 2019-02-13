#include "PA1.h"


//PA #1 TOOD: Generates a Huffman character tree from the supplied text
HuffmanTree<char>* PA1::huffmanTreeFromText(vector<string> data)
{

    //Builds a Huffman Tree from the supplied vector of strings.
    //This function implement's Huffman's Algorithm as specified in the
    //book.

    //In order for your tree to be the same as mine, you must take care 
    //to do the following:
    //1.	When merging the two smallest subtrees, make sure to place the 
    //      smallest tree on the left side!
	//store frequencies in hashtable

    // freq distribution
    unordered_map<char, int> frequencies;
    
    for(auto word : data)
    {
        for(auto ch : word)
        {
            frequencies[ch]++;
        }
    }

	//maintains huffman tree forest 
    priority_queue <HuffmanTree<char>*, vector<HuffmanTree<char>*>, 
                    TreeComparer> forest;

    // need to loop
    for(auto kvp : frequencies)
    {
        forest.push(new HuffmanTree<char>(kvp.first, kvp.second));
    }

    // place smaller on left side
    //  merge trees continously until 1 tree
    while(!forest.empty())
    {
        if(forest.size()==1)
        {
            break;
        }

        HuffmanTree<char>* smaller = forest.top();
        forest.pop();
        HuffmanTree<char>* larger = forest.top();
        forest.pop();
        forest.push(new HuffmanTree<char>{smaller, larger});
    }

    //TODO: shouldn't return nullptr
    return forest.top();
}



//PA #1 TODO: Generates a Huffman character tree from the supplied encoding map
//NOTE: I used a recursive helper function to solve this!

// honestly not sure what this task is asking
// whats the difference between this function and the encoding function?
// in class: buiding nodes 

void huffmanTreeFromMapHelper(HuffmanNode<char>& node)
{
    HuffmanNode<char>* _root = new HuffmanInternalNode<char>{nullptr, nullptr};
    HuffmanInternalNode<char>* current = dynamic_cast<HuffmanInternalNode<char>*>(root);
    HuffmanTree<char>* right;
}

HuffmanTree<char>* PA1::huffmanTreeFromMap(unordered_map<char, string> huffmanMap)
{
    //Generates a Huffman Tree based on the supplied Huffman Map.Recall that a 
    //Huffman Map contains a series of codes(e.g. 'a' = > 001).Each digit(0, 1) 
    //in a given code corresponds to a left branch for 0 and right branch for 1.

    // what we did during claas: 
    HuffmanNode<char>* _root = nullptr;
    string path = "0110";

    HuffmanNode<char>* root = new HuffmanInternalNode<char>{nullptr, nullptr};
    HuffmanInternalNode<char>* current = dynamic_cast<HuffmanInternalNode<char>*>(root);
    HuffmanTree<char>* right;

    //  in the loop we are creating the internal nodes
    for(int i =0; i<path.length()-1; i++)
    {
        char ch = path[i];
        if (ch == '0')
        {
            // left
            if(current->getLeftChild() == nullptr)
            {
                current->setLeftChild(new HuffmanInternalNode<char>{nullptr, nullptr});
            }
            current = dynamic_cast<HuffmanInternalNode<char>*>(current->getLeftChild());
        }
        else 
        {
            // right
            if(current->getRightChild() == nullptr)
            {
                current->setRightChild(new HuffmanInternalNode<char>{nullptr, nullptr});
            }
            current = dynamic_cast<HuffmanInternalNode<char>*>(current->getRightChild());
        }
    }

    // outside of the loop we are creating leaf nodes 
    char last_ch = path[path.length()-1];

    if(last_ch == '0')
    {
        current->setLeftChild(new HuffmanLeafNode<char>{value, 1});
    }
    else
    {
        current->setRightChild(new HuffmanLeafNode<char>{value, 1});
    }
    


    return nullptr;
}


void huffmanEncodingMapFromTreeHelper(unordered_map<char, string>& map, 
    HuffmanNode<char>* node,
    string encoding)
    {
        if(!node->isLeaf())
        {
            // not a leaf, make recursive calls
            HuffmanInternalNode<char>* root = dynamic_cast<HuffmanInternalNode<char>*>(node);

            huffmanEncodingMapFromTreeHelper(map, root->getLeftChild(), encoding + "0");
            huffmanEncodingMapFromTreeHelper(map, root->getRightChild(), encoding + "1");
            return;
        }
        else
        {
            // this is a leaf. this means that we have a complete mapping for this character

            // this converts node, which is a HuffmanNode into a leaf node
            // dynamic cast converts type that we want, what we want to convert
            HuffmanLeafNode<char>* root = dynamic_cast<HuffmanLeafNode<char>*>(node);
            map[root->getValue()] = encoding;
            return; 
        }
        
    }


//PA #1 TODO: Generates a Huffman encoding map from the supplied Huffman tree
//NOTE: I used a recursive helper function to solve this!
unordered_map<char, string> PA1::huffmanEncodingMapFromTree(HuffmanTree<char> *tree)
{
    // a pre-order walk 

    unordered_map<char, string> result;

    huffmanEncodingMapFromTreeHelper(result, tree->getRoot(), "");

    return result;
}

//PA #1 TODO: Writes an encoding map to file.  Needed for decompression.
void PA1::writeEncodingMapToFile(unordered_map<char, string> huffmanMap, string file_name)
{
    //Writes the supplied encoding map to a file.  My map file has one 
    //association per line (e.g. 'a' and 001 would yield the line "a001")
    ofstream writeFile(file_name);

    if(writeFile.is_open())
    {
        for(auto kvp : huffmanMap)
        {
            writeFile << kvp.first << kvp.second << endl;

        }

    }
    else
    {
        cout << "unable to open";
    }
    
    writeFile.close();
}

//PA #1 TODO: Reads an encoding map from a file.  Needed for decompression.
unordered_map<char, string> PA1::readEncodingMapFromFile(string file_name)
{
    //Creates a Huffman Map from the supplied file.Essentially, this is the 
    //inverse of writeEncodingMapToFile.  
    ifstream readFile(file_name);
    readFile.open(file_name);

    // not understanding what this is asking, So it will convert the file into a map
    // where it counts the characters? 
    if(readFile.is_open()==true)
    {
        string line =" ";
        while(!readFile.good())
        {
            getline(readFile, line);
        }
    }
    unordered_map<char, string> result{};
    return result;
}

//PA #1 TODO: Converts a vector of bits (bool) back into readable text using the supplied Huffman map
string PA1::decodeBits(vector<bool> bits, unordered_map<char, string> huffmanMap)
{
    // calll the build tree from map, call the tree and walk the tree 
    new HuffmanTree<char>* = huffmanTreeFromMap()

    //Uses the supplied Huffman Map to convert the vector of bools (bits) back into text.
    //To solve this problem, I converted the Huffman Map into a Huffman Tree and used 
    //tree traversals to convert the bits back into text.
    ostringstream result{};
    return result.str();
}

//PA #1 TODO: Using the supplied Huffman map compression, converts the supplied text into a series of bits (boolean values)
vector<bool> PA1::toBinary(vector<string> text, unordered_map<char, string> huffmanMap)
{
    // look up the string representation
    
    vector<bool> result{};
    return result;
}