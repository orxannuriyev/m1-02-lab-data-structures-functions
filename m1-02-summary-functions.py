def avg_resolution_by_category(cleaned):
    totals = {}  
    counts = {} 
    for r in cleaned:
        c = r["category"]
        totals[c] = totals.get(c, 0) + r["resolution_minutes"]
        counts[c] = counts.get(c, 0) + 1
    avgs = {c: totals[c] / counts[c] for c in counts}
    return avgs, counts


avgs, counts = avg_resolution_by_category(cleaned_records)
assert sum(counts.values()) == len(cleaned_records), "There is a problem"
print("There are not any problem")



def ticket_count_per_customer(cleaned):
    per_customer = {}  

    for r in cleaned:
        cid = r["customer_id"]
        per_customer[cid] = per_customer.get(cid, 0) + 1

    return per_customer


per_customer = ticket_count_per_customer(cleaned_records)

assert sum(per_customer.values()) == len(cleaned_records), "Customer counts mismatch"





def esc_rate_overall(cleaned):
    esc = {}
    total_category = {}
    esc_category = {}

    for e in cleaned:
        s = e['escalated']
        c = e['category']

        esc[s] = esc.get(s, 0) + 1
        total_category[c] = total_category.get(c, 0) + 1

        if s:
            esc_category[c] = esc_category.get(c, 0) + 1

    true_count = esc.get(True, 0)
    false_count = esc.get(False, 0)
    total = true_count + false_count
    overall = true_count / total if total else 0

    by_category = {}
    for c in total_category:
        esc_count = esc_category.get(c, 0)
        by_category[c] = esc_count / total_category[c]

    return {
        "overall": overall,
        "by_category": by_category
    }



res = esc_rate_overall(cleaned_records)
assert 0.0 <= res["overall"] <= 1.0
assert all(0.0 <= v <= 1.0 for v in res["by_category"].values())