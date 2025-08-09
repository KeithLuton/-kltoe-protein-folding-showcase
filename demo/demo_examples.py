#!/usr/bin/env python3
"""
KLTOE Demo Examples
==================

Example runs showing different protein types and KLTOE capabilities.
Demo version only - Full implementation available under license.
"""

from kltoe_demo import KLTOEDemo

def run_examples():
    """Run demo examples for different protein types"""
    
    demo = KLTOEDemo()
    demo.show_banner()
    
    examples = [
        ("Alpha-helical peptide", "MKTAYIAKQRQISFVKSHFSRQ"),
        ("Insulin B chain", "FVNQHLCGSHLVEALYLVCGERGFFYTPKT"),
        ("Beta-forming peptide", "VKVKVKVKVKVKVKVK"),
        ("Mixed structure", "GSPATVSTYQRKFMWLNPGE")
    ]
    
    print("🧪 RUNNING KLTOE DEMO EXAMPLES")
    print("=" * 50)
    
    for i, (name, sequence) in enumerate(examples, 1):
        print(f"\n[{i}/{len(examples)}] {name}")
        print("-" * 30)
        
        result = demo.fold_protein(sequence, show_progress=False)
        
        print(f"Sequence: {sequence}")
        print(f"Secondary Structure: {result.secondary_structure}")
        print(f"Confidence: {result.confidence:.3f}")
        print(f"Enhancement: {result.enhancement_percentage:.1f}%")
        print(f"Energy: {result.energy:.2f} kJ/mol")
        
        if i < len(examples):
            input("\nPress Enter for next example...")
    
    demo.show_licensing_info()

if __name__ == "__main__":
    run_examples()