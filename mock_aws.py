import time

def trigger_marketing_action(customer_name, predicted_segment):
    """
    This function simulates an AWS Lambda execution.
    It routes customers based on their real data tiers and RETURNS the action text.
    """
    print(f"\n⚡ [AWS Lambda Triggered] Processing customer: {customer_name}...")
    time.sleep(0.5)
    
    if predicted_segment == "Platinum":
        action =  "Triggered VIP Dedicated Account Manager Allocation + 20% Retention Credit."
    elif predicted_segment == "Gold":
        action = "Triggered High-Priority Premium Feature Upsell Email Campaign."
    elif predicted_segment == "Silver":
        action = "Triggered Bi-Weekly Standard Product Value Newsletter Sequence."
    elif predicted_segment == "Copper":
        action = "Triggered cart-abandonment reminder email + free gift on next order."
    elif predicted_segment == "Iron":
        action = "Triggered high-discount win-back email campaign (40% Off)."
    else:
        action = "General Ingestion: Added to default newsletter."
        
    print(f"✅ [Automation Success] Segment: '{predicted_segment}' -> Action Executed: {action}\n")
    
    # Return the action text so app.py can save it to the database!
    return action