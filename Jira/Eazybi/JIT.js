var EdgeLabel = ToString(issue.fields.customfield_20700).toUpperCase();
var Count = 0;
if (EdgeLabel.includes("EDGE")) {
    //issue.fields.customfield_26187 = issue.fields.customfield_26187 / 86400
    Count += 1;
    return Count;
}
