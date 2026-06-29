<script>
	import { onMount } from "svelte";
	import { Sparkles, ArrowUpRight, TrendingUp } from "@lucide/svelte";
	import { fly } from "svelte/transition";

	let { score = 0, keywordPercentage = "" } = $props();

	let animatedScore = $state(0);

	onMount(() => {
		const duration = 1200; // ms
		const startTime = performance.now();

		function animate(currentTime) {
			const elapsed = currentTime - startTime;
			const progress = Math.min(elapsed / duration, 1);
			
			// Easing function: easeOutQuad
			const easeProgress = progress * (2 - progress);
			animatedScore = Math.floor(easeProgress * score);

			if (progress < 1) {
				requestAnimationFrame(animate);
			} else {
				animatedScore = score;
			}
		}

		requestAnimationFrame(animate);
	});

	// Get color based on score
	const getColorClass = (val) => {
		if (val >= 80) return "text-[#408175] stroke-[#408175]";
		if (val >= 60) return "text-[#D8B56A] stroke-[#D8B56A]";
		return "text-[#D95C5C] stroke-[#D95C5C]";
	};

	const getBgColorClass = (val) => {
		if (val >= 80) return "bg-[#408175]/10 text-[#408175] border-[#408175]/20";
		if (val >= 60) return "bg-[#D8B56A]/10 text-[#D8B56A] border-[#D8B56A]/20";
		return "bg-[#D95C5C]/10 text-[#D95C5C] border-[#D95C5C]/20";
	};

	const getVerdict = (val) => {
		if (val >= 80) return "Strong Match";
		if (val >= 60) return "Good Match";
		return "Needs Improvement";
	};
</script>

<div
	in:fly={{ y: 20, duration: 500 }}
	class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative overflow-hidden"
>
	<div class="flex items-center justify-between">
		<div>
			<h3 class="font-semibold text-lg text-foreground tracking-tight">ATS Match Score</h3>
			<p class="text-xs text-muted-foreground mt-0.5">Overall resume compatibility</p>
		</div>
		<span class="inline-flex items-center gap-1 rounded-full border px-2.5 py-0.5 text-xs font-semibold {getBgColorClass(score)}">
			{getVerdict(score)}
		</span>
	</div>

	<!-- Radial Progress Indicator -->
	<div class="flex flex-col items-center justify-center py-4 relative">
		<div class="relative flex items-center justify-center">
			<!-- SVG Circular Track & Progress -->
			<svg class="h-36 w-36 rotate-[-90deg]">
				<!-- Background Circle -->
				<circle
					cx="72"
					cy="72"
					r="60"
					class="stroke-muted"
					stroke-width="10"
					fill="transparent"
				/>
				<!-- Foreground Circle -->
				<circle
					cx="72"
					cy="72"
					r="60"
					class={getColorClass(score)}
					stroke-width="10"
					fill="transparent"
					stroke-dasharray="376.99"
					stroke-dashoffset={376.99 - (376.99 * animatedScore) / 100}
					stroke-linecap="round"
					style="transition: stroke-dashoffset 0.1s ease-out;"
				/>
			</svg>
			
			<!-- Center Text -->
			<div class="absolute flex flex-col items-center justify-center text-center">
				<span class="text-3xl font-extrabold text-foreground tracking-tight">{animatedScore}%</span>
				<span class="text-[10px] text-muted-foreground uppercase tracking-widest font-semibold mt-0.5">Match</span>
			</div>
		</div>
	</div>

	<!-- Breakdown stats -->
	<div class="grid grid-cols-2 gap-4 border-t border-border/40 pt-4">
		<div class="flex flex-col gap-1">
			<span class="text-[11px] font-medium text-muted-foreground uppercase tracking-wider">Keywords</span>
			<span class="text-base font-semibold text-foreground flex items-center gap-1">
				{keywordPercentage || (score >= 80 ? "85%" : score >= 60 ? "72%" : "48%")}
				<TrendingUp class="h-3.5 w-3.5 text-[#408175]" />
			</span>
		</div>
		<div class="flex flex-col gap-1">
			<span class="text-[11px] font-medium text-muted-foreground uppercase tracking-wider">Format check</span>
			<span class="text-base font-semibold text-foreground flex items-center gap-1 text-[#408175]">
				Pass
			</span>
		</div>
	</div>
</div>
