<script>
	import { CheckCircle2, AlertCircle, XCircle, Info, ChevronDown, ChevronUp } from "@lucide/svelte";
	import { slide } from "svelte/transition";

	let {
		items = [
			{ id: 1, name: "File Format", status: "pass", desc: "PDF format is highly readable by ATS parsers." },
			{ id: 2, name: "Contact Info", status: "pass", desc: "Found valid email address and phone number." },
			{ id: 3, name: "Page Count", status: "pass", desc: "Your resume is 1 page long, which is optimal." },
			{ id: 4, name: "Action Verbs", status: "warn", desc: "Some bullet points lack action verbs (e.g. 'Responsible for...')." },
			{ id: 5, name: "Section Headers", status: "pass", desc: "Standard headers (Experience, Skills, Education) were detected." },
			{ id: 6, name: "Quantifiable Impact", status: "fail", desc: "Missing metrics or key performance indicators (KPIs) in 3 bullet points." }
		]
	} = $props();

	let expandedId = $state(null);

	function toggleExpand(id) {
		if (expandedId === id) {
			expandedId = null;
		} else {
			expandedId = id;
		}
	}
</script>

<div class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative">
	<div>
		<h3 class="font-semibold text-lg text-foreground tracking-tight">Resume Quality Checklist</h3>
		<p class="text-xs text-muted-foreground mt-0.5">Automated layout and content checks</p>
	</div>

	<div class="divide-y divide-border/40">
		{#each items as item}
			<div class="py-3 first:pt-0 last:pb-0">
				<!-- Header Clickable Row -->
				<button
					onclick={() => toggleExpand(item.id)}
					class="flex w-full items-center justify-between gap-4 text-left focus:outline-none group"
				>
					<div class="flex items-center gap-3">
						{#if item.status === "pass"}
							<CheckCircle2 class="h-5 w-5 text-[#408175] shrink-0" />
						{:else}
							<AlertCircle class="h-5 w-5 {item.status === 'warn' ? 'text-[#D8B56A]' : 'text-[#D95C5C]'} shrink-0" />
						{/if}
						<span class="font-medium text-sm text-foreground group-hover:text-[#408175] transition-colors">{item.name}</span>
					</div>

					<div class="flex items-center gap-2">
						<span class="text-xs font-semibold capitalize
							{item.status === 'pass' ? 'text-[#408175]' : ''}
							{item.status === 'warn' ? 'text-[#D8B56A]' : ''}
							{item.status === 'fail' ? 'text-[#D95C5C]' : ''}
						">
							{item.status === "pass" ? "Passed" : item.status === "warn" ? "Warning" : "Critical"}
						</span>
						{#if expandedId === item.id}
							<ChevronUp class="h-4 w-4 text-muted-foreground" />
						{:else}
							<ChevronDown class="h-4 w-4 text-muted-foreground group-hover:text-foreground transition-colors" />
						{/if}
					</div>
				</button>

				<!-- Collapsible Content -->
				{#if expandedId === item.id}
					<div transition:slide={{ duration: 200 }} class="mt-2 pl-8 pr-4">
						<p class="text-xs text-muted-foreground leading-relaxed bg-muted/30 p-2.5 rounded-lg border border-border/40">
							{item.desc}
						</p>
					</div>
				{/if}
			</div>
		{/each}
	</div>
</div>
