#include <iostream>
#include <map>
#include <string>
#include <climits>
#include <cmath>
#include<iomanip>
using namespace std;

// ── Preset Sizes ──────────────────────────────────────────
map<string, pair<int,int>> YOUTUBE_SIZES = {
    { "tv"        , {2560, 1440} },
    { "desktop"   , {2560, 423}  },
    { "tablet"    , {1855, 423}  },
    { "mobile"    , {1546, 423}  },
    { "safe_area" , {1546, 423}  }
};


// ── Find Closest Preset ───────────────────────────────────
string findClosestPreset(int userW, int userH) {

    long long userArea    = (long long)userW * userH;
    long long minDiff     = LLONG_MAX;
    string    closestName = "";

    cout << "\n📐 User Input Area : " << userW << " x " << userH
         << " = " << userArea << " px\n";
    cout << "\n----------------------------------------------\n";
    cout << left
         << setw(14) << "Preset"
         << setw(16) << "Size"
         << setw(14) << "Area"
         << setw(12) << "Difference" << "\n";
    cout << "----------------------------------------------\n";

    for (auto& [name, size] : YOUTUBE_SIZES) {
        long long presetArea = (long long)size.first * size.second;
        long long diff       = abs(userArea - presetArea);

        cout << setw(14) << name
             << setw(6)  << size.first << " x "
             << setw(6)  << size.second
             << setw(14) << presetArea
             << setw(12) << diff << "\n";

        if (diff < minDiff) {
            minDiff     = diff;
            closestName = name;
        }
    }

    cout << "----------------------------------------------\n";
    return closestName;
}


// ── Main ──────────────────────────────────────────────────
int main() {

    cout << "========================================\n";
    cout << "     Find Closest YouTube Banner Size\n";
    cout << "========================================\n";

    int w, h;
    cout << "\nEnter your image width  (px) : "; cin >> w;
    cout << "Enter your image height (px) : "; cin >> h;

    string result = findClosestPreset(w, h);

    auto [rw, rh] = YOUTUBE_SIZES[result];
    cout << "\n✅ Closest Preset : " << result
         << "  (" << rw << " x " << rh << ")\n\n";

    return 0;
}



