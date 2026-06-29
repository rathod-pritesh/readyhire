<script>
	import { Lightbulb, ArrowRight, Check, X, AlertTriangle } from "@lucide/svelte";
	import { fly } from "svelte/transition";

	let {
		improvements = [
			{
				category: "Experience Section",
				title: "Add measurable impact to Svelte development",
				problem: "Worked on Svelte components and fixed styling bugs.",
				solution: "Built 12+ reusable Svelte 5 components, reducing code duplication by 25% and fixing critical rendering bugs to improve UI speed by 15%.",
				reason: "ATS algorithms and hiring managers favor quantifiable achievements over tasks."
			},
			{
				category: "Summary Section",
				title: "Highlight key framework expertise early",
				problem: "Frontend developer looking for a job in Svelte/JavaScript.",
				solution: "Results-driven Frontend Engineer with 3+ years of expertise in Svelte, JavaScript, and Tailwind CSS. Specializing in highly performant, accessible web apps.",
				reason: "A strong profile summary grabs immediate attention and establishes core expertise."
			},
			{
				category: "Skills Section",
				title: "Group skills by competency",
				problem: "Svelte, JavaScript, HTML, CSS, Git, Docker, Jest.",
				solution: "Frontend: Svelte, JavaScript, HTML/CSS | Tooling & Testing: Git, Docker, Jest",
				reason: "Categorizing skills improves readability for human recruiters scanning in 6 seconds."
			}
		]
	} = $props();
</script>

<div
	in:fly={{ y: 20, duration: 500, delay: 100 }}
	class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative"
>
	<div>
		<h3 class="font-semibold text-lg text-foreground tracking-tight flex items-center gap-2">
			Content Optimizations
			<Lightbulb class="h-4.5 w-4.5 text-[#D8B56A]" />
		</h3>
		<p class="text-xs text-muted-foreground mt-0.5">Rewrite suggestions to maximize ATS and recruiter appeal</p>
	</div>

	<div class="flex flex-col gap-6">
		{#each improvements as imp}
			<div class="flex flex-col gap-3 rounded-xl border border-border/80 bg-muted/10 p-5 hover:border-[#408175]/30 transition-all duration-300">
				<!-- Header -->
				<div class="flex items-center justify-between gap-2">
					<span class="text-[10px] font-semibold uppercase tracking-wider text-[#B5B9F0] bg-[#B5B9F0]/5 px-2 py-0.5 rounded border border-[#B5B9F0]/10">
						{imp.category}
					</span>
					<span class="text-xs text-muted-foreground flex items-center gap-1">
						<AlertTriangle class="h-3 w-3 text-[#D8B56A]" />
						Recommended
					</span>
				</div>

				<h4 class="font-semibold text-sm text-foreground">{imp.title}</h4>

				<!-- Before & After comparisons -->
				<div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-2">
					<!-- Before -->
					<div class="flex flex-col gap-1.5 rounded-lg bg-[#D95C5C]/5 border border-[#D95C5C]/15 p-3 text-xs">
						<div class="flex items-center gap-1 text-[#D95C5C] font-semibold">
							<X class="h-3.5 w-3.5" />
							<span>Original</span>
						</div>
						<p class="text-muted-foreground italic leading-relaxed">"{imp.problem}"</p>
					</div>

					<!-- After -->
					<div class="flex flex-col gap-1.5 rounded-lg bg-[#408175]/5 border border-[#408175]/15 p-3 text-xs">
						<div class="flex items-center gap-1 text-[#408175] font-semibold">
							<Check class="h-3.5 w-3.5" />
							<span>Suggested Rewrite</span>
						</div>
						<p class="text-foreground font-medium leading-relaxed">"{imp.solution}"</p>
					</div>
				</div>

				<!-- Rationale -->
				<p class="text-xs text-muted-foreground mt-1 border-t border-border/40 pt-2.5">
					<span class="font-semibold text-foreground">Why:</span> {imp.reason}
				</p>
			</div>
		{/each}
	</div>
</div>
