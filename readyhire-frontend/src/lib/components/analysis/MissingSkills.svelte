<script>
	import { AlertTriangle, PlusCircle, ArrowRight } from "@lucide/svelte";
	import { fly } from "svelte/transition";

	let {
		skills = [
			{ name: "TypeScript", type: "Hard Skill", importance: "Critical", reason: "Required for robust application architecture" },
			{ name: "CI/CD Pipelines", type: "Hard Skill", importance: "Secondary", reason: "Automated deployment processes" },
			{ name: "Unit Testing (Jest/Vitest)", type: "Hard Skill", importance: "Secondary", reason: "Ensuring code quality and test coverage" },
			{ name: "Agile/Scrum Methodologies", type: "Soft Skill", importance: "Optional", reason: "Standard team collaboration model" }
		]
	} = $props();

	const getImportanceColor = (imp) => {
		if (imp === "Critical") return "bg-[#D95C5C]/10 text-[#D95C5C] border-[#D95C5C]/20";
		if (imp === "Secondary") return "bg-[#D8B56A]/10 text-[#D8B56A] border-[#D8B56A]/20";
		return "bg-[#1A1A1A] text-[#BFC3C8] border-border/40";
	};
</script>

<div
	in:fly={{ y: 20, duration: 500, delay: 200 }}
	class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative overflow-hidden"
>
	<div>
		<h3 class="font-semibold text-lg text-foreground tracking-tight flex items-center gap-2">
			Skill Gaps & Priority
		</h3>
		<p class="text-xs text-muted-foreground mt-0.5">
			Skills mentioned in the job description but not clearly identified in your resume
		</p>
	</div>

	<!-- List of missing skills -->
	<div class="flex flex-col gap-3">
		{#each skills as skill}
			<div class="flex flex-col sm:flex-row sm:items-center justify-between border border-border/60 bg-muted/20 hover:bg-muted/40 rounded-xl p-4 gap-3 transition-colors duration-200">
				<div class="flex items-start gap-3">
					<div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-background text-muted-foreground border border-border/80">
						<PlusCircle class="h-4.5 w-4.5 text-[#408175]" />
					</div>
					<div>
						<div class="flex items-center gap-2">
							<span class="font-semibold text-sm text-foreground">{skill.name}</span>
							<span class="text-[10px] text-muted-foreground">({skill.type})</span>
						</div>
						<p class="text-xs text-muted-foreground mt-0.5 leading-relaxed">{skill.reason}</p>
					</div>
				</div>

				<span class="inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium self-start sm:self-center {getImportanceColor(skill.importance)}">
					{skill.importance}
				</span>
			</div>
		{/each}
	</div>
</div>
