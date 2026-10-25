import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = {}
    num_pages = len(corpus)

    links = corpus.get(page, set())

    # If page has no outgoing links, choose uniformly among all pages
    if not links:
        for p in corpus:
            distribution[p] = 1.0 / num_pages
        return distribution

    # Base random probability for every page
    base_prob = (1.0 - damping_factor) / num_pages
    link_prob = damping_factor / len(links)

    for p in corpus:
        distribution[p] = base_prob
        if p in links:
            distribution[p] += link_prob

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    counts = {p: 0 for p in corpus}
    pages = list(corpus.keys())

    # First sample chosen uniformly at random
    current_page = random.choice(pages)
    counts[current_page] += 1

    # Remaining n - 1 samples chosen based on transition model
    for _ in range(n - 1):
        probs = transition_model(corpus, current_page, damping_factor)
        page_choices = list(probs.keys())
        weights = list(probs.values())
        current_page = random.choices(page_choices, weights=weights, k=1)[0]
        counts[current_page] += 1

    return {p: count / n for p, count in counts.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    n = len(corpus)
    ranks = {p: 1.0 / n for p in corpus}

    while True:
        new_ranks = {}
        for p in corpus:
            incoming_sum = 0
            for i in corpus:
                # If a page has no links, it links to all pages in the corpus
                if len(corpus[i]) == 0:
                    incoming_sum += ranks[i] / n
                elif p in corpus[i]:
                    incoming_sum += ranks[i] / len(corpus[i])

            new_ranks[p] = ((1.0 - damping_factor) / n) + (damping_factor * incoming_sum)

        diff = max(abs(new_ranks[p] - ranks[p]) for p in corpus)
        ranks = new_ranks
        if diff <= 0.001:
            break

    # Normalize to ensure values sum to 1
    total = sum(ranks.values())
    return {p: rank / total for p, rank in ranks.items()}


if __name__ == "__main__":
    main()
