<script>
	import { FileText, Copy, Check, Sparkles } from "@lucide/svelte";
	import { fade } from "svelte/transition";

	let {
		draft = `Dear Hiring Manager,

I am writing to express my strong interest in the Frontend Developer position at your company. With a solid foundation in responsive web design, interactive user interfaces, and modular component architectures, I am excited about the opportunity to contribute to your engineering team.

My technical background is centered on building high-performance web applications using JavaScript, HTML, CSS, and Svelte. During my recent work, I built several reusable Svelte components that reduced codebase duplication and resolved rendering performance bottlenecks. I also have experience designing responsive user interfaces with Tailwind CSS and integrating complex RESTful APIs.

I am particularly drawn to this role because it aligns with my passion for creating intuitive, accessible user experiences. I am eager to apply my experience in Svelte and Tailwind CSS to help build your next-generation frontends.

Thank you for your time and consideration. I look forward to the possibility of discussing how my skills and experience align with your team's needs.

Sincerely,
[Your Name]`
	} = $props();

	let copied = $state(false);

	function handleCopy() {
		navigator.clipboard.writeText(draft);
		copied = true;
		setTimeout(() => {
			copied = false;
		}, 2000);
	}
</script>

<div class="flex flex-col gap-6 rounded-2xl border border-border bg-card p-6 shadow-sm transition-all duration-300 relative">
	<div class="flex items-center justify-between gap-4">
		<div>
			<h3 class="font-semibold text-lg text-foreground tracking-tight flex items-center gap-2">
				Cover Letter Generator
				<Sparkles class="h-4 w-4 text-[#B5B9F0]" />
			</h3>
			<p class="text-xs text-muted-foreground mt-0.5">AI-generated starting draft tailored to the job description</p>
		</div>

		<!-- Copy Button -->
		<button
			onclick={handleCopy}
			class="inline-flex h-9 items-center justify-center gap-1.5 rounded-lg border border-border bg-background px-3 text-xs font-medium text-muted-foreground hover:bg-muted hover:text-foreground transition-all active:scale-[0.98]"
			aria-label="Copy draft"
		>
			{#if copied}
				<Check class="h-3.5 w-3.5 text-[#408175]" />
				<span class="text-[#408175]">Copied!</span>
			{:else}
				<Copy class="h-3.5 w-3.5" />
				<span>Copy Draft</span>
			{/if}
		</button>
	</div>

	<!-- Preview Textarea/Container -->
	<div class="relative rounded-xl border border-border/80 bg-muted/30 p-5 font-mono text-xs text-foreground leading-relaxed max-h-[300px] overflow-y-auto whitespace-pre-line select-text">
		{draft}
		<!-- Gradient fade at the bottom if content is long -->
		<div class="sticky bottom-0 left-0 right-0 h-8 bg-gradient-to-t from-muted/30 to-transparent pointer-events-none"></div>
	</div>
</div>
