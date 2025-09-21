import argparse, sys
from .storage import add_entry, load_entries, clear_entries, delete_entry, search_entries
from .stats import mean_length

def main(argv=None):
    parser = argparse.ArgumentParser(prog="ship1", description="Edge Labs — Ship Log (Python) - Enhanced")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="add a new entry")
    p_add.add_argument("text", nargs="+", help="entry text")

    sub.add_parser("list", help="list entries (newest first)")

    p_clear = sub.add_parser("clear", help="clear the log")
    p_clear.add_argument("-y", "--yes", action="store_true", help="do not prompt")

    sub.add_parser("stats", help="show count and mean entry length")

    # New commands for Ship 1
    p_delete = sub.add_parser("delete", help="delete an entry by index")
    p_delete.add_argument("index", type=int, help="1-based index of entry to delete")

    p_search = sub.add_parser("search", help="search entries containing text")
    p_search.add_argument("query", help="text to search for")

    ns = parser.parse_args(argv)

    if ns.cmd == "add":
        text = " ".join(ns.text).strip()
        if not text:
            print("Nothing to add.", file=sys.stderr)
            return 2
        add_entry(text)
        print("OK: added")
        return 0

    if ns.cmd == "list":
        entries = load_entries()
        if not entries:
            print("(no entries yet)")
            return 0
        # TODO: Update list command to show numbered entries with timestamps
        for i, e in enumerate(entries, 1):
            print(f"{i}. {e['t']} — {e['v']}")
        for e in entries:
            print(f"{e['t']} — {e['v']}")
        return 0

    if ns.cmd == "clear":
        if not ns.yes:
            ans = input("This will erase all entries. Continue? [y/N] ").strip().lower()
            if ans not in ("y", "yes"):
                print("Aborted.")
                return 1
        clear_entries()
        print("Cleared.")
        return 0

    if ns.cmd == "stats":
        entries = load_entries()
        n = len(entries)
        avg = mean_length([e["v"] for e in entries]) if entries else 0.0
        print(n)
        print(f"{avg:.2f}")
        print(f"Count: {n} | Mean length: {avg:.2f} chars")
        return 0

    if ns.cmd == "delete":
        # TODO: Implement delete command
        success = delete_entry(ns.index)
        if success:
            print(f"Deleted entry {ns.index}")
            return 0
        else:
            print(f"Error: Entry {ns.index} does not exist", file=sys.stderr)
            return 1
        print("Delete command not implemented yet")
        return 1

    if ns.cmd == "search":
        # TODO: Implement search command
        results = search_entries(ns.query)
        if not results:
            print(f"No entries found containing '{ns.query}'")
            return 0
        print(f"Found {len(results)} entries:")
        for i, entry in enumerate(results, 1):
            print(f"{i}. {entry['t']} — {entry['v']}")
            return 0
        print("Search command not implemented yet")
        return 1

    parser.print_help()
    return 2

if __name__ == "__main__":
    sys.exit(main())
