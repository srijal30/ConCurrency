"""
checks the commited blockchain snapshot info
"""

from model.loader import load_snapshot

def pubkeyTooLong(pem: str) -> str:
    lines = [line for line in pem.splitlines() if "-----" not in line]
    if not lines:
        return "<no-key>"
    core = "".join(lines)
    return core[:10] + "..." + core[-10:]


def main():
    #load from disk
    try:
        snap = load_snapshot("committed_snapshot.data")
    except Exception as e:
        print("[INSPECT] Failed to load committed_snapshot.data:", e)
        return

    if not snap.accounts:
        print("[INSPECT] No accounts in snapshot.")
        return

    print("[INSPECT] Accounts in committed snapshot:")
    print("----------------------------------------")
    for pubkey_pem, account in snap.accounts.items():
        ident = pubkeyTooLong(pubkey_pem)
        print(
            f"account={ident} | balance={account.balance} | sequence={account.sequence}"
        )


if __name__ == "__main__":
    main()
