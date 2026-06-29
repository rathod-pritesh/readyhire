<script>
	import { MessageSquare, HelpCircle, ChevronDown, ChevronUp, Star } from "@lucide/svelte";
	import { slide } from "svelte/transition";

	let {
		questions = [
			{
				id: 1,
				question: "You've worked heavily with Svelte, but how do you approach state management in large scale applications?",
				tip: "Mention Svelte's stores, context API, and Svelte 5's new runes ($state, $derived, $effect) for fine-grained reactivity. Talk about modularizing global stores vs local component state.",
				difficulty: "Medium"
			},
			{
				id: 2,
				question: "This job description lists TypeScript. Can you explain your experience with TS and how you handle complex types?",
				tip: "Explain that while your recent projects used JavaScript, you understand type safety. Discuss concepts like interfaces, union types, and generics, and express eagerness to work with TypeScript.",
				difficulty: "Hard"
			},
			{
				id: 3,
				question: "How do you ensure web accessibility (a11y) when styling components using Tailwind CSS?",
				tip: "Discuss semantic HTML, ARIA attributes, keyboard navigation (tabindex, focus styles), and leveraging Tailwind's screen-reader (sr-only) or active/focus-visible utilities.",
				difficulty: "Medium"
			}
		]
	} = $props();

	let activeId = $state(null);

	function toggleTip(id) {
		if (activeId === id) {
			activeId = null;
		} else {
			activeId = id;
		}
	}

	const getDifficultyColor = (diff) => {
		if (diff === "Hard") return "bg-[#D95C5C]/10 text-[#D95C5C] border-[#D95C5C]/20";
		if (diff === "Medium") return "bg-[#D8B56A]/10 text-[#D8B56A] border-[#D8B56A]/20";
		return "bg-[#408175]/10 text-[#408175] border-[#408175]/20";
	};
</script>

<div class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative">
	<div>
		<h3 class="font-semibold text-lg text-foreground tracking-tight flex items-center gap-2">
			Tailored Interview Prep
			<MessageSquare class="h-4.5 w-4.5 text-[#408175]" />
		</h3>
		<p class="text-xs text-muted-foreground mt-0.5">Mock questions likely to be asked based on your resume profile and this role</p>
	</div>

	<div class="flex flex-col gap-4">
		{#each questions as q}
			<div class="rounded-xl border border-border bg-muted/20 hover:bg-muted/40 transition-colors duration-200 overflow-hidden">
				<!-- Question Button -->
				<button
					onclick={() => toggleTip(q.id)}
					class="flex w-full items-start justify-between gap-4 p-4 text-left focus:outline-none group"
				>
					<div class="flex gap-3">
						<HelpCircle class="h-5 w-5 text-[#408175]" />
						<div class="space-y-1">
							<p class="text-sm font-semibold text-foreground group-hover:text-[#408175] transition-colors leading-relaxed">
								{q.question}
							</p>
							<span class="inline-flex items-center rounded-full border px-2 py-0.5 text-[10px] font-medium {getDifficultyColor(q.difficulty)}">
								{q.difficulty} Difficulty
							</span>
						</div>
					</div>

					{#if activeId === q.id}
						<ChevronUp class="h-4.5 w-4.5 text-muted-foreground shrink-0 mt-1" />
					{:else}
						<ChevronDown class="h-4.5 w-4.5 text-muted-foreground group-hover:text-foreground transition-colors shrink-0 mt-1" />
					{/if}
				</button>

				<!-- Answer Tip -->
				{#if activeId === q.id}
					<div transition:slide={{ duration: 250 }} class="border-t border-border/40 bg-muted/40 p-4 text-xs">
						<h5 class="font-bold text-foreground mb-1.5 flex items-center gap-1">
							<Star class="h-3.5 w-3.5 text-[#D8B56A] fill-[#D8B56A]" />
							Suggested Answer Strategy
						</h5>
						<p class="text-muted-foreground leading-relaxed">
							{q.tip}
						</p>
					</div>
				{/if}
			</div>
		{/each}
	</div>
</div>
