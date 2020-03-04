/*
思路：对字符串进行遍历，begin指向字符串首字母索引，end指向空格的前一个位置。
如果碰到空格，对begin与end之间的单词进行翻转.
注意：每次判断为空格时，begin要在空格的位置基础上加1，指向空格后下一个单词的首字母。最后一个单词末尾无空格，也需要翻转。
*/

#include <iostream>
#include <string>

using namespace std;


string reverseWords(string s) {
    int begin=0,end;
    for(int i=0,len=s.length(); i<len+1; i++){
        if(s[i] == ' '||s[i] == '\0'){
            for(end=i-1;begin<end;begin++,end--){
                swap(s[begin],s[end]);
            }
            begin=i+1;
        }
    }

    return s;
}


int main(){
    string s;
    getline(cin, s);
    cout<<s<<endl;
    cout<<reverseWords(s)<<endl;
    return 0;
}