<script>
	import { CheckCircle2, XCircle, Search, Sparkles } from "@lucide/svelte";
	import { fly } from "svelte/transition";

	let { 
		matching = ["JavaScript", "Svelte", "Tailwind CSS", "CSS", "HTML", "REST APIs", "Git"], 
		missing = ["TypeScript", "GraphQL", "Vite", "Jest", "CI/CD", "Docker"] 
	} = $props();

	let filter = $state("all"); // 'all', 'matching', 'missing'

	const filteredMatching = $derived(filter === "missing" ? [] : matching);
	const filteredMissing = $derived(filter === "matching" ? [] : missing);
	const totalCount = $derived(matching.length + missing.length);
</script>

<div
	in:fly={{ y: 20, duration: 500, delay: 100 }}
	class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative overflow-hidden"
>
	<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
		<div>
			<h3 class="font-semibold text-lg text-foreground tracking-tight flex items-center gap-2">
				ATS Keyword Analysis
				<Sparkles class="h-4 w-4 text-[#B5B9F0]" />
			</h3>
			<p class="text-xs text-muted-foreground mt-0.5">
				Found {matching.length} of {totalCount} relevant keywords in your resume
			</p>
		</div>

		<!-- Filter Buttons -->
		<div class="inline-flex rounded-lg border border-border bg-muted/50 p-1 self-start sm:self-center">
			<button
				onclick={() => (filter = "all")}
				class="rounded-md px-3 py-1 text-xs font-medium transition-all {filter === 'all' ? 'bg-background text-foreground shadow-sm' : 'text-muted-foreground hover:text-foreground'}"
			>
				All
			</button>
			<button
				onclick={() => (filter = "matching")}
				class="rounded-md px-3 py-1 text-xs font-medium transition-all {filter === 'matching' ? 'bg-background text-foreground shadow-sm' : 'text-muted-foreground hover:text-foreground'}"
			>
				Matching ({matching.length})
			</button>
			<button
				onclick={() => (filter = "missing")}
				class="rounded-md px-3 py-1 text-xs font-medium transition-all {filter === 'missing' ? 'bg-background text-foreground shadow-sm' : 'text-muted-foreground hover:text-foreground'}"
			>
				Missing ({missing.length})
			</button>
		</div>
	</div>

	<!-- Keywords Grid -->
	<div class="flex flex-wrap gap-2.5 max-h-[220px] overflow-y-auto pr-1">
		{#each filteredMatching as kw}
			<div class="inline-flex items-center gap-1.5 rounded-full border border-[#408175]/20 bg-[#408175]/5 px-3.5 py-1 text-xs font-medium text-[#408175] shadow-sm transition-colors duration-200">
				<CheckCircle2 class="h-3.5 w-3.5" />
				{kw}
			</div>
		{/each}

		{#each filteredMissing as kw}
			<div class="inline-flex items-center gap-1.5 rounded-full border border-[#D95C5C]/20 bg-[#D95C5C]/5 px-3.5 py-1 text-xs font-medium text-[#D95C5C] shadow-sm transition-colors duration-200">
				<XCircle class="h-3.5 w-3.5" />
				{kw}
			</div>
		{/each}

		{#if filteredMatching.length === 0 && filteredMissing.length === 0}
			<div class="flex flex-col items-center justify-center py-6 text-center w-full">
				<p class="text-sm text-muted-foreground">No keywords match the selected filter.</p>
			</div>
		{/if}
	</div>

	<!-- Insight Callout -->
	<div class="rounded-xl border border-[#B5B9F0]/20 bg-[#B5B9F0]/5 p-4 text-xs text-[#B5B9F0] flex items-start gap-3">
		<Search class="h-4.5 w-4.5 shrink-0 mt-0.5" />
		<div>
			<span class="font-semibold">ATS Recommendation:</span> Integrate the missing keywords naturally in your project descriptions or skills sections to rank higher for this role.
		</div>
	</div>
</div>
