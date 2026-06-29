<script>
	import { Check } from "@lucide/svelte";
	import { fly } from "svelte/transition";

	let {
		categories = [
			{ name: "Frontend Development", skills: ["Svelte", "JavaScript", "Tailwind CSS", "HTML", "CSS"], rating: 85 },
			{ name: "APIs & Databases", skills: ["REST APIs", "SQL", "Node.js"], rating: 65 },
			{ name: "Tools & DevOps", skills: ["Git", "GitHub", "VS Code"], rating: 90 }
		]
	} = $props();
</script>

<div
	in:fly={{ y: 20, duration: 500, delay: 300 }}
	class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative overflow-hidden"
>
	<div>
		<h3 class="font-semibold text-lg text-foreground tracking-tight">Identified Skill Categories</h3>
		<p class="text-xs text-muted-foreground mt-0.5">Skills extracted and verified from your resume</p>
	</div>

	<div class="flex flex-col gap-5">
		{#each categories as cat}
			<div class="space-y-2">
				<div class="flex justify-between items-center text-sm font-medium">
					<span class="text-foreground font-semibold">{cat.name}</span>
					<span class="text-xs text-muted-foreground">{cat.rating}% Strength</span>
				</div>

				<!-- Progress bar -->
				<div class="h-2 w-full rounded-full bg-muted overflow-hidden">
					<div 
						class="h-full bg-gradient-to-r from-[#2E4540] to-[#408175] rounded-full" 
						style="width: {cat.rating}%"
					></div>
				</div>

				<!-- Skill tags -->
				<div class="flex flex-wrap gap-1.5 pt-1">
					{#each cat.skills as skill}
						<span class="inline-flex items-center gap-1 rounded-md bg-muted px-2.5 py-0.5 text-xs text-foreground font-medium border border-border/40">
							<Check class="h-3 w-3 text-[#408175]" />
							{skill}
						</span>
					{/each}
				</div>
			</div>
		{/each}
	</div>
</div>
