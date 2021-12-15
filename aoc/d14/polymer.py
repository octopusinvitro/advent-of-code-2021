class Polymer():
    def __init__(self, template, rules):
        self._template = template
        self._rules = rules

    def element_counts(self, steps):
        element_counts, pair_counts = self._load_template()

        for step in range(steps):
            element_counts, pair_counts = self._run_step(element_counts, pair_counts)

        return element_counts

    def _load_template(self):
        template_pairs = zip(self._template, self._template[1:])
        element_counts = {}
        pair_counts = {}

        for first, last in template_pairs:
            self._increment(pair_counts, first + last)
            self._increment(element_counts, first)

        self._increment(element_counts, last)

        return (element_counts, pair_counts)

    def _run_step(self, element_counts, pair_counts):
        new_pair_counts = {}

        for pair, insertion in self._rules.items():
            count = pair_counts.get(pair, None)
            if not count:
                continue

            first, last = pair
            self._increment(new_pair_counts, first + insertion, count)
            self._increment(new_pair_counts, insertion + last, count)
            self._increment(element_counts, insertion, count)

        return (element_counts, new_pair_counts)

    def _increment(self, dictionary, key, count=1):
        dictionary[key] = dictionary.get(key, 0) + count
