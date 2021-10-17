// Generated from MyGrammer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MyGrammerParser}.
 */
public interface MyGrammerListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code LetterExpr}
	 * labeled alternative in {@link MyGrammerParser#s}.
	 * @param ctx the parse tree
	 */
	void enterLetterExpr(MyGrammerParser.LetterExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LetterExpr}
	 * labeled alternative in {@link MyGrammerParser#s}.
	 * @param ctx the parse tree
	 */
	void exitLetterExpr(MyGrammerParser.LetterExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InfixExpr}
	 * labeled alternative in {@link MyGrammerParser#s}.
	 * @param ctx the parse tree
	 */
	void enterInfixExpr(MyGrammerParser.InfixExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InfixExpr}
	 * labeled alternative in {@link MyGrammerParser#s}.
	 * @param ctx the parse tree
	 */
	void exitInfixExpr(MyGrammerParser.InfixExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LineExpr}
	 * labeled alternative in {@link MyGrammerParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLineExpr(MyGrammerParser.LineExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LineExpr}
	 * labeled alternative in {@link MyGrammerParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLineExpr(MyGrammerParser.LineExprContext ctx);
}